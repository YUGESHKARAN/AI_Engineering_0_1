def build_context(documents):

    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "unknown"
        )

        page = document.metadata.get(
            "page",
            "unknown"
        )

        context_parts.append(
            f"""
                Source: {source}
                Page: {page}

                {document.page_content}
            """
        )

    return "\n\n---\n\n".join(
        context_parts
    )


def build_prompt(
    question: str,
    context: str
):

    return f"""
You are a helpful question-answering assistant.

Answer the user's question using only the
provided context.

If the answer cannot be found in the context,
say:

"I don't know based on the provided document."

Do not invent information.

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
"""