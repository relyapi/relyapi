import tldextract


def extract_main_domain(host: str) -> str:
    """
    提取主域名，例如：
    'api.dev.taobao.com' -> 'taobao.com'
    """
    result = tldextract.extract(host)
    if not result.domain or not result.suffix:
        return host  # 无法提取时返回原始 host
    return f"{result.domain}.{result.suffix}"
