
from typing import List

from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_NAMESPACE,
)
from ingestion.embeddings import PineconeEmbedding


# Initialize Pinecone client
pc = Pinecone(
    api_key=PINECONE_API_KEY
)


def get_vector_store() -> PineconeVectorStore:
    """Return the configured Pinecone vector store."""

    index = pc.Index(
        PINECONE_INDEX_NAME
    )

    return PineconeVectorStore(
        index=index,
        embedding=PineconeEmbedding(),
        namespace=PINECONE_NAMESPACE,
    )


def retrieve_documents(
    question: str,
    document_id: str,
    top_k: int = 3,
) -> List[Document]:
    """
    Retrieve the most relevant chunks for a question,
    filtered to a specific document.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if not document_id.strip():
        raise ValueError("Document ID cannot be empty.")

    vector_store = get_vector_store()

    documents = vector_store.similarity_search(
        query=question,
        k=top_k,
        filter={
            "document_id": {
                "$eq": document_id
            }
        },
    )

    return documents