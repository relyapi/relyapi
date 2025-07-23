import socketio
from loguru import logger

sio = socketio.AsyncServer(
    # 兼容分布式场景
    # client_manager=socketio.AsyncRedisManager(
    #     f'redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}/{settings.REDIS_DATABASE}'
    # ),
    async_mode='asgi',
    cors_allowed_origins='*',
    ping_interval=10,
    ping_timeout=5,
)


@sio.event
async def disconnect(sid: str):
    """
    设备断联事件
    """
    logger.info(f'Client {sid} disconnected')


@sio.event
async def register(sid, data):
    """
    设备连接，向server发送注册信息
    """
    logger.info(f'Client {sid} registered: {data}')
