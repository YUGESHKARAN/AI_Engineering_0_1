from pathlib import Path

from .loader import load_document
from .chunker import split_documents
from .vector_store import get_vector_store


def ingest_document(
    file_path: str,
    document_id: str
):

    # 1. Load
    documents = load_document(file_path)

    # 2. Add common document ID
    for document in documents:

        document.metadata["document_id"] = document_id

        document.metadata["source"] = Path(
            file_path
        ).name

    # 3. Chunk
    chunks = split_documents(documents)

    # 4. Add chunk metadata
    for index, chunk in enumerate(chunks):

        chunk.metadata["chunk_index"] = index

    # 5. Store in Pinecone
    vector_store = get_vector_store()

    ids = [
        f"{document_id}#chunk_{index}"
        for index in range(len(chunks))
    ]

    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )

    return {
        "document_id": document_id,
        "chunks": len(chunks),
        "source": Path(file_path).name
    }