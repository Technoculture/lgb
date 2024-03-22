"""
Provide access to different embeddings models
"""

import os
from abc import ABC, abstractmethod
from openai import OpenAI  # type: ignore


class EmbeddingsModel(ABC):
    @abstractmethod
    def get_embedding(self, text: str) -> list[float]:
        pass


class OpenAIEmbeddingsModel(EmbeddingsModel):
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
        self.model="text-embedding-3-small"

    def get_embedding(self, text: str) -> list[float]:
        text = text.replace("\n", " ")
        return (
            self.client.embeddings.create(
                input=[text], model=model, dimensions=384, encoding_format="float"
            )
            .data[0]
            .embedding
        )