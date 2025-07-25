import os
from contextlib import asynccontextmanager

import socketio
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

from app.router import router
from plugins import load_plugins
from utils.common_utils import get_local_ip
from utils.exceptions import register_exception

load_dotenv()
sio_client: socketio.AsyncClient = socketio.AsyncClient(
    reconnection=True,
    reconnection_attempts=5,
    reconnection_delay=1
)
RELY_SOCKETIO_ADDRESS = os.environ.get('RELY_SOCKETIO_ADDRESS', 'http://127.0.0.1:8500')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 加载插件
    load_plugins(os.getcwd())
    await sio_client.connect(RELY_SOCKETIO_ADDRESS)
    await sio_client.emit("register", {"ip": get_local_ip()})

    logger.info("Startup event is done.")

    yield
    await sio_client.disconnect()
    logger.info("shutdown event is done.")


app = FastAPI(root_path='/rely/worker', lifespan=lifespan)


@app.get("/healthz")
def healthz() -> str:
    return "ok"


register_exception(app)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
