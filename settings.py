# from functools import lru_cache
# from typing import Any
#
# from pydantic_settings import BaseSettings, SettingsConfigDict
#
#
# class Settings(BaseSettings):
#     # redis
#     REDIS_HOST: str
#     REDIS_PORT: int
#     REDIS_PASSWORD: str
#     REDIS_DATABASE: int
#     REDIS_TIMEOUT: int = 5
#     DEVICE_LOCK_PREFIX: str = 'device_lock:'
#     DEFAULT_LOCK_TTL: int = 300
#
#     # mysql
#     MYSQL_HOST: str
#     MYSQL_PORT: int
#     MYSQL_USER: str
#     MYSQL_PASSWORD: str
#     MYSQL_SCHEMA: str
#     DATABASE_CHARSET: str = 'utf8mb4'
#
#     FASTAPI_API_V1_PATH: str = '/api/v1'
#
#     # celery
#     CELERY_BROKER_REDIS_DATABASE: int = 1
#     CELERY_BACKEND_REDIS_DATABASE: int = 2
#     CELERY_BACKEND_REDIS_PREFIX: str = 'device:celery:'
#     CELERY_BACKEND_REDIS_TIMEOUT: int = 5
#     CELERY_TASK_MAX_RETRIES: int = 5
#     CELERY_TASK_PACKAGES: list[str] = ['app.task.celery_task']
#     # Celery 定时任务配置
#     CELERY_SCHEDULE: dict[str, dict[str, Any]] = {
#         'exec-every-10-seconds': {
#             'task': 'listen_queue_async',
#             'schedule': 10,
#         },
#     }
#
#     DATABASE_ECHO: bool = False
#     DATABASE_POOL_ECHO: bool = False
#
#     # date
#     DATETIME_TIMEZONE: str = 'Asia/Shanghai'
#     DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
#
#     QUEUE_PREFIX: str = 'device_queue:'
#     LOCK_PREFIX: str = 'device_lock:'
#     LOCK_TILL: str = '300'
#     RETRY_COUNT_PREFIX: str = 'retry_count:'
#     RETRY_COUNT_TILL: str = '300'
#     RETRY_COUNT: str = '5'
#     SYNC_LOCK: str = 'sync_lock'
#
#     model_config = SettingsConfigDict(env_file='.env')
#
#
# @lru_cache
# def get_settings() -> Settings:
#     """获取全局配置单例"""
#     return Settings()
#
#
# settings = get_settings()
