from plugins import BasePlugin, RequestModel


class BaiduPlugin(BasePlugin):
    domain = "www.baidu.com"

    def invoke(self, url, method, headers, body=None) -> RequestModel:
        return RequestModel(url=url, method=method, headers=headers, json=body)
