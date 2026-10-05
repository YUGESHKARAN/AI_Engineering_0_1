from typing import List

from pinecone import Pinecone

from config import PINECONE_API_KEY


pc = Pinecone(api_key=PINECONE_API_KEY)


class PineconeEmbedding:

    def embed_documents(
        self,
        texts: List[str]
    ) -> List[List[float]]:

        response = pc.inference.embed(
            model="llama-text-embed-v2",
            inputs=[
                {"text": text}
                for text in texts
            ],
            parameters={
                "input_type": "passage",
                "truncate": "END",
                "dimension": 512,
            },
        )

        return [
            item["values"]
            for item in response
        ]

    def embed_query(
        self,
        text: str
    ) -> List[float]:

        response = pc.inference.embed(
            model="llama-text-embed-v2",
            inputs=[
                {"text": text}
            ],
            parameters={
                "input_type": "query",
                "truncate": "END",
                "dimension": 512,
            },
        )

        return response[0]["values"]