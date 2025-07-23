import httpx
from fastapi import Request, APIRouter
from httpx import Proxy
from loguru import logger
from starlette.responses import Response

from plugins import plugin_manager
from utils.common_utils import extract_main_domain
from utils.exceptions import HttpxCallFail
from utils.plugin_invoker import PluginInvoker
from utils.tls_utils import tls_factory

router = APIRouter(
    prefix='/proxy',
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

    result = await plugin_invoker.invoke(
        plugin, url, method, headers, body,
        timeout=5,
        use_process=False  # 切换 True 试试强隔离
    )

    # 按域名配置开关 代理
    # 将数据再次转发到serverless进行处理
    # 提供插件 那么就是 header信息的填充
    # tls统一进行处理修改 借鉴 https://curl-cffi.readthedocs.io/en/latest/impersonate.html
    # https://github.com/vgavro/httpx-curl-cffi

    #
    # 使用隧道代理 封装隧道代理 根据用户名自行返回代理
    # 不使用tls直接配置代理
    proxy = Proxy("http://127.0.0.1:7897")

    # client: httpx.AsyncClient = request.app.state.client

    try:
        async with httpx.AsyncClient(
                proxy=proxy if plugin.use_proxy else None,
                transport=tls_factory(proxy) if plugin.use_tls else None
        ) as client:
            resp = await client.request(**result.model_dump(by_alias=True))
            if "application/json" in resp.headers.get("content-type", ""):
                return resp.json()
            else:
                return Response(
                    content=resp.content,
                    status_code=resp.status_code,
                    media_type=resp.headers.get("content-type", "application/octet-stream")
                )
    except Exception as e:
        logger.error(e)
        raise HttpxCallFail(e)
