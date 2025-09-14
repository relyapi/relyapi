import os

import httpx
from fastapi import Request, APIRouter
from loguru import logger
from relyapi.invoke import PluginInvoker
from relyapi.plugin import BypassType
from starlette.responses import Response

from utils.common_utils import extract_main_domain
from utils.exceptions import HttpxCallFail
from utils.plugin import CommonPlugin
from utils.plugin import plugin_manager
from utils.tls_utils import tls_factory

router = APIRouter(
    prefix='/bypass',
    tags=['透传服务'],
    responses={404: {'description': 'Not found'}},
)

plugin_invoker = PluginInvoker()


@router.post("/forward")
async def forward(request: Request):
    """
    代理转发
    :param request:
    :return:
    """
    data = await request.json()
    method = data["method"]
    url = data["url"]
    headers = data.get("headers") or {}
    body = data.get("body") or {}

    domain = extract_main_domain(url)

    logger.info(f"domain: {domain}")

    x_rely_timeout = headers.get("x-rely-timeout") or 5
    # 支持的协议："http", "https", "socks5", "socks5h"
    # http://user:pwd@ip:port
    # 外部如果传递ip，使用relyapi随机ip，当请求的网站是国内网站将使用国内ip，否则使用国外ip
    x_rely_proxy = headers.get("x-rely-proxy", os.environ.get('RELY_TUNNEL_PROXY'))
    logger.info(f"x_rely_proxy: {x_rely_proxy}")

    # 使用redis   使用 socket.io 是不是好管理
    plugin = plugin_manager.get(domain) or CommonPlugin()

    result = await plugin_invoker.invoke(
        plugin, url, method, headers, body
    )

    try:
        async with httpx.AsyncClient(
                proxy=x_rely_proxy if plugin.use_proxy and plugin.bypass_type == BypassType.RAW else None,
                transport=tls_factory(x_rely_proxy) if plugin.bypass_type == BypassType.TLS else None,
                timeout=x_rely_timeout,
                verify=False
        ) as client:
            resp = await client.request(**result.model_dump(by_alias=True))
            return Response(
                content=resp.content,
                status_code=resp.status_code,
                media_type=resp.headers.get("content-type", "application/octet-stream")
            )

    except Exception as e:
        logger.error(e)
        raise HttpxCallFail(e)
