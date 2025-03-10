from fastapi import FastAPI
from datetime import datetime
import json
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    sages_env = os.getenv("SAGES")

    with open("/config/config.txt", "r") as f:
        config = f.read()

    with open("/config/plik.txt", "r") as f:
        plik = f.read()

    with open("/config/zmienna.txt", "r") as f:
        zmienna = f.read()

    return {"time": current_time, "sages": sages_env, "config": config, "plik": plik, "zmienna": zmienna}
