from fastapi import FastAPI
from datetime import datetime
import time

app = FastAPI()

start_time = time.time()

@app.get("/ping")
async def ping():
    time_diff = time.time() - start_time

    if time_diff > 30:
        raise Exception("TEST")

    return {"time": datetime.now().isoformat()}
