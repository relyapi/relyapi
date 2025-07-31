import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from utils.context_vars import request_id_var


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request_id_var.set(request_id)  # 设置上下文
        response = await call_next(request)
        response.headers["x-request-id"] = request_id
        return response
