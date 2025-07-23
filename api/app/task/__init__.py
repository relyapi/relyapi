import socketio

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
