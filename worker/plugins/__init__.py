import importlib
import os
from typing import Dict, Optional

from loguru import logger
from pydantic import BaseModel

from utils.exceptions import DomainNotFound


class RequestModel(BaseModel):
    method: str
    url: str
    headers: Optional[Dict[str, str]] = {}
    json: Optional[Dict] = None


class BasePlugin:
    domain = ""

    def invoke(self, url, method, headers, body=None) -> RequestModel:
        raise NotImplementedError("Subclasses must implement this method")


class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, BasePlugin] = {}

    def register(self, crawler):
        if not issubclass(crawler, BasePlugin):
            raise TypeError(f"{crawler.__name__} 必须继承自 BasePlugin")
        instance_obj = crawler()
        if isinstance(instance_obj.domain, list):
            for domain in instance_obj.domain:
                self.plugins[domain] = instance_obj
        else:
            self.plugins[instance_obj.domain] = instance_obj

    def get(self, domain: str) -> BasePlugin:
        plugin = self.plugins.get(domain)
        if plugin is None:
            raise DomainNotFound()
        return plugin


plugin_manager = PluginManager()


def load_plugins(plugins_path):
    logger.info(f"Loading plugins from {plugins_path}")
    for filename in os.listdir(os.path.join(plugins_path, "plugins")):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"plugins.{filename[:-3]}"
            module = importlib.import_module(module_name)

            for attr_name in dir(module):
                attr: BasePlugin = getattr(module, attr_name)
                if (
                        isinstance(attr, type)
                        and issubclass(attr, module.BasePlugin)
                        and attr is not module.BasePlugin
                ):
                    logger.info(f"Loading {attr.__class__.__name__} from {module_name}")
                    plugin_manager.register(attr)
