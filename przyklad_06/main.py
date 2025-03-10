from fastapi import FastAPI
from datetime import datetime
import json
import os

app = FastAPI()

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()

    with open("/katalog/time.json", "w") as f:
        json.dump({"time": current_time}, f)

    with open("/katalog_2/time.json", "w") as f:
        json.dump({"time": current_time}, f)

    with open("/katalog_3/time.json", "w") as f:

    return {"time": current_time}
