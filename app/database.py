from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

import os
from sqlmodel import SQLModel

from app.models import Document
from app.vectorstore import add_to_vecstore

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_FILE = os.path.join(DATA_DIR, "rag_app.sqlite")

# Async engine
engine: AsyncEngine = create_async_engine(
    f"sqlite+aiosqlite:///{DB_FILE}", echo=False, future=True
)

# Session factory
async_session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def seed():
    samples = [
        {
            "title": "Intro to Product A",
            "content": "Product A is an electric toothbrush launched in 2024. Key specs: battery 2000mAh, price 49.99, colors: white, black.",
            "source": "internal_manual",
        },
        {
            "title": "Q2 Sales Report 2025",
            "content": "Q2 2025 total revenue: 1,200,000 USD. Top region: APAC. Top product: Product A, revenue 400,000 USD.",
            "source": "reports",
        },
        {
            "title": "FAQ - Returns",
            "content": "Return policy: 30 days from purchase. Items must be in original packaging. Refunds issued within 7 business days.",
            "source": "support",
        },
        # add more useful demo docs or load from CSV
    ]

    async with async_session_factory() as session:
        for s in samples:
            d = Document(
                title=s["title"],
                content=s["content"],
                source=s["source"]
            )
            session.add(d)
            await session.flush()  # get ID before commit

            # 🔹 push immediately into vectorstore
            await add_to_vecstore(d)
        await session.commit()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
