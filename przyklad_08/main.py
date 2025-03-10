from fastapi import FastAPI
from datetime import datetime
import json
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    with open("/run/secrets/my_secret", "r") as f:
        secret = f.read()

    with open("/run/secrets/token", "r") as f:
        token = f.read()

    return {"time": current_time, "secret": secret, "token": token}
