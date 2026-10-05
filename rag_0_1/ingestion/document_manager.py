from .vector_store import get_index
from config import (
    PINECONE_NAMESPACE
)

from .ingest import ingest_document


def delete_document(document_id: str):

    index = get_index()

    index.delete(
        namespace=PINECONE_NAMESPACE,
        filter={
            "document_id": {
                "$eq": document_id
            }
        }
    )

    return {
        "document_id": document_id,
        "status": "deleted"
    }





def update_document(
    file_path: str,
    document_id: str
):

    index = get_index()

    # Delete old chunks
    index.delete(
        namespace=PINECONE_NAMESPACE,
        filter={
            "document_id": {
                "$eq": document_id
            }
        }
    )

    # Ingest new version
    return ingest_document(
        file_path=file_path,
        document_id=document_id
    )