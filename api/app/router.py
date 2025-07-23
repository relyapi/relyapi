from fastapi import APIRouter

from app.rely.proxy import router as proxy_router

router = APIRouter()
router.include_router(proxy_router)
