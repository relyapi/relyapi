from app.admin.proxy import router as proxy_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(proxy_router)
