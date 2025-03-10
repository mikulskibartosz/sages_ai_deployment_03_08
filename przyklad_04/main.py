from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
async def ping():
    with open("content.txt", "r") as f:
        content = f.read()

    current_time = datetime.now().isoformat()

    return {"time": current_time, "content": content}
