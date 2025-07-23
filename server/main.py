import socketio
import uvicorn
from fastapi import FastAPI

from app.task import sio

app = FastAPI(root_path='/rely/server')

socket_app = socketio.ASGIApp(sio, app)

if __name__ == '__main__':
    config = uvicorn.Config(app=socket_app, host='0.0.0.0', port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()
