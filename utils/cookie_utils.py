from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def replace_query_param(url: str, key: str, value: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query[key] = [value]  # 替换或添加 key
    new_query = urlencode(query, doseq=True)
    new_url = parsed._replace(query=new_query)
    return urlunparse(new_url)


def replace_cookie(cookie_str: str, key: str, new_value: str) -> str:
    cookie = SimpleCookie()
    cookie.load(cookie_str)
    cookie[key] = new_value
    return "; ".join([f"{k}={v.value}" for k, v in cookie.items()])


if __name__ == '__main__':
    url = "https://example.com/path?foo=1&bar=2"
    new_url = replace_query_param(url, "foo", "999")
    print(new_url)
    # 输出: https://example.com/path?foo=999&bar=2
