import os
from contextlib import asynccontextmanager

import httpx
import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.router import router
from plugins import load_plugins
from utils.exceptions import register_exception


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 加载插件
    load_plugins(os.getcwd())
    app.state.client = httpx.AsyncClient()

    logger.info("Startup event is done.")

    yield

    await app.state.client.aclose()
    logger.info("shutdown event is done.")


app = FastAPI(root_path='/rely/worker', lifespan=lifespan)


@app.get("/healthz")
def healthz() -> str:
    return "ok"


register_exception(app)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
