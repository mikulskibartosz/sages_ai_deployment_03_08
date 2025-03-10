from fastapi import FastAPI
from datetime import datetime
import httpx

app = FastAPI()

@app.get("/ping")
async def ping():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://backend:8000/ping")
        response_json = response.json()

    return {"time": datetime.now().isoformat(), "response": response_json}
