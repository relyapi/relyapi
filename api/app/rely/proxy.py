import httpx
from fastapi import APIRouter, Request

router = APIRouter(
    prefix='/proxy',
    tags=['代理服务'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/forward")
async def forward(request: Request):
    data = await request.json()
    method = data["method"]
    url = data["url"]
    headers = data.get("headers", {})
    body = data.get("body", None)

    # 将数据再次转发到serverless进行处理
    async with httpx.AsyncClient() as client:
        resp = await client.request(method, url, headers=headers, content=body)
        return resp.content  # 自动透传
