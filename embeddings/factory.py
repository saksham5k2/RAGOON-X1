from embeddings.sentence_transformer import SentenceTransformerEmbedding


class EmbeddingFactory:

    @staticmethod
    def create(model_name: str):
        return SentenceTransformerEmbedding(model_name)