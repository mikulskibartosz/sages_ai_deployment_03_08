from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"time": datetime.now().isoformat()}
