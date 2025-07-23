from relyapi import Client

client = Client()

resp = client.get("https://httpbin.org/get")
print(resp.json())
