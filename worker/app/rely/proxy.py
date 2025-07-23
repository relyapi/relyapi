import httpx
from fastapi import APIRouter, Request
from loguru import logger

from plugins import plugin_manager
from utils.domain import extract_main_domain

router = APIRouter(
    prefix='/proxy',
    tags=['代理服务'],
    responses={404: {'description': 'Not found'}},
)


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
    result = plugin.invoke(url, method, headers, body)

    # 将数据再次转发到serverless进行处理
    # 提供插件 那么就是 header信息的填充
    # tls统一进行处理修改 借鉴 https://curl-cffi.readthedocs.io/en/latest/impersonate.html
    async with httpx.AsyncClient() as client:
        resp = await client.request(**result.model_dump())
        return resp.content
