import hashlib

import tldextract
from tenacity import retry, stop_after_attempt, wait_exponential

retry_strategy = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)


def extract_main_domain(host: str) -> str:
    """
    提取主域名，例如：
    'api.dev.taobao.com' -> 'taobao.com'
    """
    result = tldextract.extract(host)
    if not result.domain or not result.suffix:
        return host  # 无法提取时返回原始 host
    return f"{result.domain}.{result.suffix}"


def gen_md5(content):
    md5 = hashlib.md5()
    md5.update(content.encode())
    return md5.hexdigest()
