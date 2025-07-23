import httpx
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/forward")
async def forward(request: Request):
    data = await request.json()
    method = data["method"]
    url = data["url"]
    headers = data.get("headers", {})
    body = data.get("body", None)

    async with httpx.AsyncClient() as client:
        resp = await client.request(method, url, headers=headers, content=body)
        return resp.content  # 自动透传


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
