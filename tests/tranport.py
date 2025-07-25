import os

import httpx

RELY_API_ADDRESS = os.environ.get("RELY_API_ADDRESS", 'http://127.0.0.1:8000')

# RELY_API_ADDRESS = os.environ.get("RELY_API_ADDRESS", 'http://49.232.171.141:8001')


class ForwardingTransport(httpx.BaseTransport):
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        payload = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": request.read().decode("utf-8") if request.content else None
        }

        # 将请求内容转发到你自己的服务
        forward_resp = httpx.post(f"{RELY_API_ADDRESS}/rely/worker/bypass/forward", json=payload)

        # 构造 httpx.Response 返回给上层
        return httpx.Response(
            status_code=forward_resp.status_code,
            headers=forward_resp.headers,
            content=forward_resp.content,
            request=request
        )


class AsyncForwardingTransport(httpx.AsyncBaseTransport):
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        payload = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "body": await request.aread()
        }

        async with httpx.AsyncClient() as client:
            forward_resp = await client.post("http://127.0.0.1:9000/rely/worker/bypass/forward", json=payload)

        return httpx.Response(
            status_code=forward_resp.status_code,
            headers=forward_resp.headers,
            content=forward_resp.content,
            request=request
        )
