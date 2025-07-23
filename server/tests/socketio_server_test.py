#!/usr/bin/env python
import socketio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi')
combined_asgi_app = socketio.ASGIApp(sio, app)


@app.get('/')
async def hello():
    return {'message': 'Hello, World!'}


@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')
    await sio.emit('hello', (1, 2, {'hello': 'you'}), to=sid)


@sio.event
def disconnect(sid):
    print('disconnected', sid)


if __name__ == '__main__':
    uvicorn.run(combined_asgi_app, host='127.0.0.1', port=5000)
