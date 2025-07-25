from app.task.api.account import router as account_router
from app.task.api.proxy import router as proxy_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(proxy_router)
router.include_router(account_router)
