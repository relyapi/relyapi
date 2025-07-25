from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, msg: str, code: int):
        self.msg = msg
        self.code = code


class DomainNotFound(UnicornException):
    def __init__(self):
        super().__init__("Domain not found", 301)


class HttpxCallFail(UnicornException):
    def __init__(self, err_msg):
        super().__init__(err_msg, 302)


def register_exception(app: FastAPI):
    """
    异常
    """

    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'msg': f'{exc.msg}', 'data': None, 'code': exc.code}),
        )

    @app.exception_handler(RequestValidationError)
    async def request_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'msg': exc, 'data': None, 'code': 500}),
        )

    @app.exception_handler(ResponseValidationError)
    async def response_exception_handler(request: Request, exc: ResponseValidationError):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'msg': exc.errors(), 'data': None, 'code': 500}),
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder({'msg': exc, 'data': None, 'code': 500}),
        )
