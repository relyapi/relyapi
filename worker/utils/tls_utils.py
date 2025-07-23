import httpx
from curl_cffi import CurlOpt

from utils.transport import AsyncCurlTransport


def tls_factory(proxy: httpx.Proxy):
    transport = AsyncCurlTransport(
        impersonate="chrome",
        proxy=proxy,
        default_headers=True,
        # required for parallel requests, see curl_cffi issues below
        curl_options={CurlOpt.FRESH_CONNECT: True})

    return transport
