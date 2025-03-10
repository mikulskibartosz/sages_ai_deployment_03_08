from fastapi import FastAPI
from datetime import datetime
import json
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    katalog_env = os.getenv("KATALOG")
    sages_env = os.getenv("SAGES")

    return {"time": current_time, "katalog": katalog_env, "sages": sages_env}
