from fastapi import APIRouter

from app.proxy.forward import router as proxy_router

router = APIRouter()
router.include_router(proxy_router)
