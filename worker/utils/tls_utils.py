from curl_cffi import CurlOpt
from httpx import Proxy

from utils.transport import AsyncCurlTransport


def tls_factory(proxy: str):
    proxy = Proxy(proxy) if proxy else None

    transport = AsyncCurlTransport(
        impersonate="chrome",
        proxy=proxy,
        default_headers=True,
        # required for parallel requests, see curl_cffi issues below
        curl_options={CurlOpt.FRESH_CONNECT: True})

    return transport
