import hashlib


def gen_md5(content):
    md5 = hashlib.md5()
    md5.update(content.encode())
    return md5.hexdigest()
