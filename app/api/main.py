from fastapi import FastAPI
from app.api.routers.auth_router import router as auth_router
from app.infrastructure.repositories.db import engine, Base

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)