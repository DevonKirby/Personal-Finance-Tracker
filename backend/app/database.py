from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
from app.config import settings

engine = create_async_engine(settings.database_url)                 # Creates PostgreSQL connection
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)   # Factory that produces sessions

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

