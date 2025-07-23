from relyapi import Client

client = Client()

# resp = client.get("https://httpbin.org/get")
resp = client.get("https://www.baidu.com")
print(resp.json())
