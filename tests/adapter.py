import requests
from requests.adapters import HTTPAdapter
from requests.models import Response


class ProxyAdapter(HTTPAdapter):
    def send(self, request, **kwargs):
        # 构造原始请求内容
        payload = {
            "method": request.method,
            "url": request.url,
            "headers": dict(request.headers),
            "body": request.body.decode() if hasattr(request.body, 'decode') else request.body
        }

        # 转发到你的 HTTP 服务
        forward_url = "http://127.0.0.1:9000/forward"
        print(f"[FORWARD] {request.method} {request.url} => {forward_url}")
        resp = requests.post(forward_url, json=payload)

        # 将你的服务返回的响应构造成 Response 对象
        r = Response()
        r.status_code = resp.status_code
        r.headers = resp.headers
        r._content = resp.content
        r.url = request.url
        return r
