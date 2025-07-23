import socketio
import uvicorn
from fastapi import FastAPI

from app.router import router
from app.task import sio
from utils.exception import register_exception

app = FastAPI(root_path='/rely')

register_exception(app)

app.include_router(router)

socket_app = socketio.ASGIApp(sio, app)

if __name__ == '__main__':
    config = uvicorn.Config(app=socket_app, host='0.0.0.0', port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()
