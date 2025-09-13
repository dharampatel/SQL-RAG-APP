from typing import List
from sqlmodel import select
from app.models import Document
from app.database import async_session_factory
from app.vectorstore import add_to_vecstore


async def create_doc(title: str, content: str, source: str = None) -> Document:
    async with async_session_factory() as session:
        doc = Document(title=title, content=content, source=source)
        session.add(doc)
        await session.commit()
        await session.refresh(doc)

    await add_to_vecstore(doc)
    return doc


async def list_docs(limit: int = 100) -> List[Document]:
    async with async_session_factory() as session:
        result = await session.exec(select(Document).limit(limit))
        return result.all()
