import httpx

from tranport import ForwardingTransport

client = httpx.Client(transport=ForwardingTransport())

resp = client.get("https://httpbin.org/get")
print(resp.json())
