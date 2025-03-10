from fastapi import FastAPI
from datetime import datetime
import redis

app = FastAPI()

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.get("/ping")
async def ping():
    current_time = datetime.now().isoformat()
    licznik = redis_client.incr('licznik')
    return {"time": current_time, "licznik": licznik}
