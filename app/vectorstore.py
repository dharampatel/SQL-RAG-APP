import os
import anyio
from langchain_chroma import Chroma
from langchain.schema import Document as LCDocument
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai._common import GoogleGenerativeAIError

from app.config import embed
from app.models import Document

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

PERSIST_DIR = os.path.join(DATA_DIR, "faq.db")
os.makedirs(PERSIST_DIR, exist_ok=True)

# 🔹 Global Chroma instance
_vectorstore: Chroma | None = None
_retriever = None


def get_vecstore_and_retriever():
    """
    Return the global Chroma vectorstore + retriever.
    Initializes once and reuses afterward.
    """
    global _vectorstore, _retriever

    if _vectorstore is None:
        _vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embed,
        )
        _retriever = _vectorstore.as_retriever(search_kwargs={"k": 5})

    return _vectorstore, _retriever


async def add_to_vecstore(doc: Document, chunk_size: int = 500, chunk_overlap: int = 50):
    """
    Add a single document to Chroma DB asynchronously.
    Splits large text into chunks and handles embedding errors gracefully.
    """
    vectorstore, _ = get_vecstore_and_retriever()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = text_splitter.split_text(doc.content)

    lc_docs = [
        LCDocument(
            page_content=chunk,
            metadata={
                "id": str(doc.id),
                "title": doc.title,
                "source": doc.source,
            },
        )
        for chunk in chunks
    ]

    def _add_chunks():
        for lc_doc in lc_docs:
            try:
                vectorstore.add_documents([lc_doc])
            except GoogleGenerativeAIError as e:
                print(f"[Warning] Embedding failed for doc {doc.id} chunk: {e}")

    await anyio.to_thread.run_sync(_add_chunks)
