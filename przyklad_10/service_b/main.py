from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

random_number = random.randint(0, 100)

@app.get("/ping")
async def ping():
    return {"time": datetime.now().isoformat(), "random_number": random_number, "service": "service_b"}
