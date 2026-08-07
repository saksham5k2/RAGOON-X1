from app.settings import (
    EMBEDDING_MODEL,
    TOP_K,
    BM25_INDEX_PATH,
)

from embeddings.factory import EmbeddingFactory
from storage.factory import StorageFactory

from retrieval.factory import RetrieverFactory
from retrieval.hybrid.retriever import HybridRetriever

from retrieval.query.factory import QueryRewriterFactory
from retrieval.query.multi_query import MultiQueryGenerator
from retrieval.query.multi_retriever import MultiQueryRetriever

from reranking.factory import RerankerFactory
from compression.factory import CompressorFactory

from retrieval.stages.query_stage import QueryStage
from retrieval.stages.retrieval_stage import (
    RetrievalStageImpl,
)
from retrieval.stages.reranking_stage import (
    RerankingStage,
)
from retrieval.stages.compression_stage import (
    CompressionStage,
)
from retrieval.stages.post_processing_stage import (
    PostProcessingStage,
)


class RetrievalPipeline:

    def __init__(self):

        # -------------------------
        # Embedding Model
        # -------------------------

        embedding_model = (
            EmbeddingFactory.create(
                EMBEDDING_MODEL
            )
        )

        # -------------------------
        # Storage
        # -------------------------

        vector_store = (
            StorageFactory.create_vector_store()
        )

        sparse_store = (
            StorageFactory.create_sparse_store()
        )

        sparse_store.load(
            BM25_INDEX_PATH
        )

        # -------------------------
        # Dense Retriever
        # -------------------------

        dense = RetrieverFactory.create_dense(
            embedding_model,
            vector_store,
        )

        # -------------------------
        # Hybrid Retriever
        # Dense + BM25 + RRF
        # -------------------------

        hybrid = HybridRetriever(
            dense,
            sparse_store,
        )

        # -------------------------
        # Components
        # -------------------------

        query_rewriter = (
            QueryRewriterFactory.create()
        )

        multi_query_generator = (
            MultiQueryGenerator()
        )

        multi_query_retriever = (
            MultiQueryRetriever(
                hybrid
            )
        )

        reranker = (
            RerankerFactory.create()
        )

        compressor = (
            CompressorFactory.create()
        )

        # -------------------------
        # Retrieval Pipeline
        # -------------------------

        self.stages = [

            QueryStage(
                query_rewriter,
                multi_query_generator,
            ),

            RetrievalStageImpl(
                multi_query_retriever,
            ),

            RerankingStage(
                reranker,
            ),

            CompressionStage(
                compressor,
            ),

            PostProcessingStage(),

        ]

        self.vector_store = vector_store

    def retrieve(
        self,
        query,
        top_k=TOP_K,
    ):

        state = {
            "query": query,
            "top_k": top_k,
        }

        for stage in self.stages:

            state = stage.run(
                state
            )

        return state

    def close(self):

        self.vector_store.close()