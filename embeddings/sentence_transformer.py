from sentence_transformers import SentenceTransformer

from embeddings.base import BaseEmbeddingModel


class SentenceTransformerEmbedding(
    BaseEmbeddingModel
):

    def __init__(
        self,
        model_name: str,
    ):

        self.model = SentenceTransformer(
            model_name
        )

        self.device = self.model.device

        print(
            f"Embedding device: {self.device}"
        )

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embeddings.tolist()

    def embed_query(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            batch_size=32,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embedding.tolist()

    # -------------------------
    # Backward compatibility
    # -------------------------

    def embed(
        self,
        texts,
    ):

        return self.embed_documents(
            texts
        )