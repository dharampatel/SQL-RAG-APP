from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

from app.config import llm
from app.crud import create_doc, list_docs
from app.vectorstore import get_vecstore_and_retriever
from langchain.chains import RetrievalQA

router = APIRouter()


class DocIn(BaseModel):
    title: str
    content: str
    source: Optional[str] = None


class QueryIn(BaseModel):
    query: str
    top_k: Optional[int] = 5


@router.post("/docs", response_model=dict)
async def create_document(d: DocIn):
    doc = await create_doc(d.title, d.content, d.source)
    return {"id": doc.id, "msg": "Document saved successfully."}


@router.get("/documents", response_model=List[dict])
async def list_documents(limit: int = 100):
    docs = await list_docs(limit=limit)
    return [
        {"id": d.id, "title": d.title, "content": d.content, "source": d.source}
        for d in docs
    ]


@router.post("/query")
async def query_rag(q: QueryIn):
    vectorstore, retriever = get_vecstore_and_retriever()
    retriever.search_kwargs = {"k": q.top_k or 5}

    # Build RAG chain with sources returned
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,  # ✅ return docs!
    )

    import anyio

    def _run():
        return qa_chain.invoke({"query": q.query})

    result = await anyio.to_thread.run_sync(_run)

    # Format the response
    return {
        "query": q.query,
        "answer": result["result"],
        "sources": [
            {
                "id": doc.metadata.get("id"),
                "title": doc.metadata.get("title"),
                "source": doc.metadata.get("source"),
            }
            for doc in result["source_documents"]
        ],
    }
