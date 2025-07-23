import hashlib

import httpx
import tldextract
from tenacity import retry, stop_after_attempt, wait_exponential, wait_fixed

retry_strategy = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)


@retry(
    reraise=True,  # 保留原始异常
    stop=stop_after_attempt(3),  # 最多重试 3 次
    wait=wait_fixed(1),  # 每次失败后等待 2 秒
    # retry=retry_if_exception_type(httpx.RequestError)  # 只在网络异常时重试
)
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
