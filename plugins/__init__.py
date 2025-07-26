from typing import Dict, Any

from relyapi.plugin import RequestModel, BasePlugin
from relyapi.utils import random_ua


class CommonPlugin(BasePlugin):
    use_proxy = True
    timeout = 10

    def invoke(self, url, method, headers: Dict[str, str], body: Dict[str, Any]) -> RequestModel:
        if 'user-agent' not in headers:
            headers['user-agent'] = random_ua
        return RequestModel(url=url, method=method, headers=headers, json=body)
