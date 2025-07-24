import os

import httpx
from fastapi import Request, APIRouter
from loguru import logger
from starlette.responses import Response

from plugins import plugin_manager, BypassType, RequestModel
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
    插件会修改 添加cooKie等
    根据domain进行获取插件
    :param request:
    :return:
    """
    data = await request.json()
    method = data["method"]
    url = data["url"]
    headers = data.get("headers", {})
    body = data.get("body", None)

    domain = extract_main_domain(url)

    logger.info(f"domain: {domain}")

    plugin = plugin_manager.get(domain)
    if plugin:
        # 走账号代理池   看是否可以借鉴 openclash 进行代理  根据域名进行自动路由
        # 基于 clash 进行二次开发
        # 使用隧道代理 封装隧道代理 根据用户名自行返回代理
        # 不使用tls直接配置代理
        # 只有 use_proxy为true 才会查询代理 如果 use_proxy为false proxy直接返回空
        # 直接存储在内存 server只有一个  根据域名以及策略   domain + interface + account
        # 注意 如果涉及到 cookie 和 ip 绑定的情况  如何处理
        # 外部 http 指定需要那个账户  x-rely-account=xxx
        # 代理ip有一定的下发策略   主动查询？？ gin提供
        proxy = os.environ.get('PROXY_IP')
        result = await plugin_invoker.invoke(
            plugin, url, method, headers, body
        )
    else:
        # 兜底
        # 走普通的代理池
        proxy = None
        result = RequestModel(url=url, method=method, headers=headers, json=body)
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
