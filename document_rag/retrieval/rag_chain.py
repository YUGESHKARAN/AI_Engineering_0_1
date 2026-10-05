from langchain_groq import ChatGroq

from config import (LLM_MODEL,TOP_K)
from .retriever import retrieve_documents
from .prompt import build_context, build_prompt


def get_llm():

    return ChatGroq(
        model=LLM_MODEL,
        temperature=0
    )


def answer_question(
    question: str,
    document_id: str
):

    # 1. Retrieve
    documents = retrieve_documents(
        question=question,
        document_id=document_id,
        top_k=TOP_K
    )

    # 2. No context
    if not documents:

        return {
            "answer": (
                "I don't know based on "
                "the provided document."
            ),
            "sources": []
        }

    # 3. Build context
    context = build_context(documents)

    # 4. Build prompt
    prompt = build_prompt(
        question=question,
        context=context
    )

    # 5. Call LLM
    llm = get_llm()

    response = llm.invoke(prompt)

    # 6. Sources
    sources = []

    for document in documents:

        sources.append({
            "source": document.metadata.get(
                "source"
            ),
            "page": document.metadata.get(
                "page"
            ),
            "chunk_index": document.metadata.get(
                "chunk_index"
            )
        })

    return {
        "answer": response.content,
        "sources": sources
    }