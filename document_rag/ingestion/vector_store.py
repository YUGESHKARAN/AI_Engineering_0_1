from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_NAMESPACE,
)

from ingestion.embeddings import PineconeEmbedding


pc = Pinecone(
    api_key=PINECONE_API_KEY
)

def get_index():

    return pc.Index(
        PINECONE_INDEX_NAME
    )


def get_vector_store():

    return PineconeVectorStore(
        index=get_index(),
        embedding=PineconeEmbedding(),
        namespace=PINECONE_NAMESPACE,
    )