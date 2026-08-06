from sentence_transformers import SentenceTransformer

from embeddings.base import BaseEmbeddingModel


class SentenceTransformerEmbedding(BaseEmbeddingModel):

    def __init__(self, model_name: str):

        self.model = SentenceTransformer(model_name)

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

        return embeddings.tolist()

    def embed_query(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

        return embedding.tolist()