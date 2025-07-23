import asyncio

import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected to server')


@sio.event
async def disconnect(reason):
    print('disconnected from server, reason:', reason)


@sio.event
def hello(a, b, c):
    print(a, b, c)


async def start_server():
    await sio.connect('http://49.232.171.141:8500')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())
