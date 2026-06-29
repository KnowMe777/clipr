from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis

from .database import get_db
from .redis_client import get_redis

app = FastAPI(
    title="Clipr API",
    description="A high performance URL shprtner API"
)

@app.on_event("startup")
async def startup():
    print("Application started")

@app.get("/health")
async def health(
    db: AsyncSession = Depends(get_db),
    redis_client = Depends(get_redis)
):
    try:
        await db.execute(text("SELECT 1"))
        await redis_client.ping()

        return {"status": "ok"}
    
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Service Unavailable"
        )
