"""
# 国内 国外代理

https://github.com/gfpcom/free-proxy-list
https://www.qiyunip.com/freeProxy
https://github.com/find-xposed-magisk/go_proxy_pool/blob/main/config.yml
https://free-proxy-list.net/zh-cn/
https://github.com/yonggekkk/Cloudflare-vless-trojan
https://getfreeproxy.com/proxy-checker?p=socks4%3A%2F%2F8.213.197.208%3A8081
https://www.kuaidaili.com/free/fps/1/
https://github.com/gfpcom/free-proxy-list
https://github.com/henson/proxypool
https://github.com/zu1k/proxypool
https://github.com/jhao104/proxy_pool
"""

import asyncio
import time

import aiohttp

# 要测试的 URL
TEST_URL = "https://httpbin.org/ip"

PROXIES = [
              "socks5://127.0.0.1:8080",
          ] * 50

# 并发请求总数
TOTAL_REQUESTS = 100

# 同时运行的并发数量
CONCURRENCY = 20


async def fetch(session, url, proxy, request_id):
    try:
        start = time.time()
        async with session.get(url, proxy=proxy, timeout=10) as response:
            text = await response.text()
            print(text)
            duration = time.time() - start
            print(f"[{request_id}] ✅ Success via {proxy} in {duration:.2f}s")
            return True
    except Exception as e:
        print(f"[{request_id}] ❌ Failed via {proxy}: {e}")
        return False


async def test_proxy(proxy, total_requests, concurrency):
    print(f"\n=== Testing Proxy {proxy} with {total_requests} requests ===")
    connector = aiohttp.TCPConnector(limit_per_host=concurrency)
    async with aiohttp.ClientSession(connector=connector) as session:
        sem = asyncio.Semaphore(concurrency)
        tasks = []
        for i in range(total_requests):
            async with sem:
                task = asyncio.create_task(fetch(session, TEST_URL, proxy, i + 1))
                tasks.append(task)
        results = await asyncio.gather(*tasks)
        success_count = sum(results)
        print(f"=== Proxy {proxy} Summary: {success_count}/{total_requests} success ===")


async def main():
    tasks = [test_proxy(proxy, TOTAL_REQUESTS, CONCURRENCY) for proxy in PROXIES]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
