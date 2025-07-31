import hashlib
import socket

import httpx
import tldextract
from tenacity import retry, stop_after_attempt, wait_exponential

retry_strategy = retry(
    reraise=True,  # 保留原始异常
    stop=stop_after_attempt(3),  # 最多重试 3 次
    wait=wait_exponential(multiplier=1, min=1, max=3),
    # retry=retry_if_exception_type(httpx.RequestError)  # 只在网络异常时重试
)


@retry_strategy
async def fetch_with_retry(client: httpx.AsyncClient, result: dict):
    resp = await client.request(**result)
    return resp


def extract_main_domain(host: str) -> str:
    """
    提取域名
    """
    result = tldextract.extract(host)
    if not result.domain or not result.suffix:
        return host
    return f"{result.subdomain}.{result.domain}.{result.suffix}"


def gen_md5(content):
    md5 = hashlib.md5()
    md5.update(content.encode())
    return md5.hexdigest()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    print(f"本机内网 IP: {get_local_ip()}")
