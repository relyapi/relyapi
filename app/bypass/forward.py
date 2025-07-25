import os

import httpx
from fastapi import Request, APIRouter
from loguru import logger
from starlette.responses import Response

from plugins import plugin_manager, BypassType
from utils.common_utils import extract_main_domain, fetch_with_retry
from utils.exceptions import HttpxCallFail
from utils.plugin_invoker import PluginInvoker
from utils.tls_utils import tls_factory

router = APIRouter(
    prefix='/bypass',
    tags=['代理服务'],
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

    plugin = plugin_manager.get(domain)

    # 在 server端配置 socket.io 推送
    proxy = os.environ.get('PROXY_IP')
    result = await plugin_invoker.invoke(
        plugin, url, method, headers, body
    )

    try:
        async with httpx.AsyncClient(
                proxy=proxy if plugin.use_proxy and plugin.bypass_type == BypassType.RAW else None,
                transport=tls_factory(proxy) if plugin.bypass_type == BypassType.TLS else None,
                timeout=5
        ) as client:
            resp = await fetch_with_retry(client, result.model_dump(by_alias=True))
            return Response(
                content=resp.content,
                status_code=resp.status_code,
                media_type=resp.headers.get("content-type", "application/octet-stream")
            )

    except Exception as e:
        logger.error(e)
        raise HttpxCallFail(e)
