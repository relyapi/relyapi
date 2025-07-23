from fastapi import APIRouter
from requests.sessions import Request

router = APIRouter(
    prefix='/account',
    tags=['账户服务'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/login")
async def login(request: Request):
    """
    登录账户  下发到client 设备管理
    """
    pass
