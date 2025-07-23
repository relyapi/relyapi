import contextvars

from loguru import logger

request_id = contextvars.ContextVar("x-request-id")


def plugin_wrapper(func):
    def wrapped(*args, **kwargs):
        logger.info(f"[{request_id.get()}] Plugin start")
        return func(*args, **kwargs)

    return wrapped
