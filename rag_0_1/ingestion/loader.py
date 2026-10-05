from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredMarkdownLoader,
    CSVLoader,
)


def load_document(file_path: str):

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(str(path))

    elif extension == ".txt":
        loader = TextLoader(
            str(path),
            encoding="utf-8"
        )

    elif extension == ".docx":
        loader = Docx2txtLoader(str(path))

    elif extension == ".md":
        loader = UnstructuredMarkdownLoader(str(path))

    elif extension == ".csv":
        loader = CSVLoader(str(path))

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return loader.load()