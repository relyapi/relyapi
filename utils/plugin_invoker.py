import asyncio
import inspect
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue


class PluginInvoker:
    def __init__(self, max_threads: int = 10):
        self.executor = ThreadPoolExecutor(max_workers=max_threads)

    async def invoke(self, plugin, *args):
        """
        调用插件：支持同步/异步，线程/进程模式。
        """
        if inspect.iscoroutinefunction(plugin.invoke):
            return await self._invoke_async(plugin, *args, timeout=plugin.timeout)
        elif plugin.use_process:
            return await self._invoke_in_process(plugin, *args, timeout=plugin.timeout)
        else:
            return await self._invoke_in_thread(plugin, *args, timeout=plugin.timeout)

    async def _invoke_async(self, plugin, *args, timeout):
        return await asyncio.wait_for(plugin.invoke(*args), timeout=timeout)

    async def _invoke_in_thread(self, plugin, *args, timeout):
        loop = asyncio.get_running_loop()
        func = lambda: plugin.invoke(*args)
        return await asyncio.wait_for(
            loop.run_in_executor(self.executor, func),
            timeout=timeout
        )

    async def _invoke_in_process(self, plugin, *args, timeout):
        queue = Queue()

        def target(queue, plugin, *args):
            try:
                result = plugin.invoke(*args)
                queue.put(result)
            except Exception as e:
                queue.put({"error": str(e)})

        process = Process(target=target, args=(queue, plugin, *args))
        process.start()

        loop = asyncio.get_running_loop()
        try:
            result = await asyncio.wait_for(loop.run_in_executor(None, queue.get), timeout=timeout)
        except asyncio.TimeoutError:
            process.terminate()
            process.join()
            return {"error": "plugin timeout"}
        finally:
            if process.is_alive():
                process.terminate()
            process.join()

        return result
