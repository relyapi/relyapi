from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter(
    prefix='/proxy',
    tags=['代理服务'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/fetch")
async def fetch(request: Request):
    """
    获取代理
    """
    pass


@router.get("/config")
async def config(request: Request):
    """
    代理配置
    """
