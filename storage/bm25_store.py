import pickle

from app.settings import (
    BM25_INDEX_PATH,
)

from retrieval.sparse.index import InvertedIndex
from retrieval.sparse.bm25 import BM25


class BM25Store:

    def __init__(self):

        self.index = InvertedIndex()

        self.retriever = BM25(
            self.index
        )

    # -------------------------
    # Add Chunks
    # -------------------------

    def add(
        self,
        chunks,
    ):

        self.index.add(
            chunks
        )

    # -------------------------
    # Build + Save Index
    # -------------------------

    def build(
        self,
        chunks,
    ):

        self.add(
            chunks
        )

        self.save(
            BM25_INDEX_PATH
        )

    # -------------------------
    # Search
    # -------------------------

    def search(
        self,
        query,
        limit=10,
    ):

        return self.retriever.retrieve(
            query,
            top_k=limit,
        )

    # -------------------------
    # Save
    # -------------------------

    def save(
        self,
        path,
    ):

        with open(
            path,
            "wb",
        ) as f:

            pickle.dump(
                self.index,
                f,
            )

    # -------------------------
    # Load
    # -------------------------

    def load(
        self,
        path,
    ):

        with open(
            path,
            "rb",
        ) as f:

            self.index = pickle.load(
                f
            )

        self.retriever = BM25(
            self.index
        )

    # -------------------------
    # Close
    # -------------------------

    def close(self):

        pass