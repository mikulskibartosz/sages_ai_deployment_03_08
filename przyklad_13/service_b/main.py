from fastapi import FastAPI
from datetime import datetime
import random
import httpx
app = FastAPI()

random_number = random.randint(0, 100)

@app.get("/ping")
async def ping():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://service_a:8001/ping")
        response_json = response.json()

    return {"time": datetime.now().isoformat(), "random_number": random_number, "service": "service_b", "response": response_json}
