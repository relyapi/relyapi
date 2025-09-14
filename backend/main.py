from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from loguru import logger

from app.router import router
from utils.exceptions import register_exception

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Startup event is done.")

    yield
    logger.info("shutdown event is done.")


app = FastAPI(root_path='/api', lifespan=lifespan)


@app.get("/healthz")
def healthz() -> str:
    return "ok"


register_exception(app)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
