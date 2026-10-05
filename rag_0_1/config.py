import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

PINECONE_NAMESPACE = os.getenv(
    "PINECONE_NAMESPACE",
    "default"
)

LLM_MODEL = "openai/gpt-oss-120b"

EMBEDDING_MODEL = "llama-text-embed-v2"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

TOP_K = 3