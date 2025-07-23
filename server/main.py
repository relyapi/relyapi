import socketio
import uvicorn
from fastapi import FastAPI

from app.router import router
from app.task import sio

app = FastAPI(root_path='/rely/server')
socketio_app = socketio.ASGIApp(sio, app)


@app.get("/healthz")
def healthz() -> str:
    return "ok"


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(socketio_app, host='0.0.0.0', port=8500)
