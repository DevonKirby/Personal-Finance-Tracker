from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Personal Finance Tracker")

app.include_router(auth.router)

@app.get("/health")
async def health():
    return {"status": "ok"}