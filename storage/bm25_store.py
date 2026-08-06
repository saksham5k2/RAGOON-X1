import pickle

from retrieval.sparse.index import InvertedIndex
from retrieval.sparse.bm25 import BM25


class BM25Store:

    def __init__(self):

        self.index = InvertedIndex()

        self.retriever = BM25(
            self.index
        )

    def add(self, chunks):

        self.index.add(chunks)

    def search(
        self,
        query,
        limit=10,
    ):

        return self.retriever.retrieve(
            query,
            top_k=limit,
        )

    def save(
        self,
        path,
    ):

        with open(path, "wb") as f:
            pickle.dump(
                self.index,
                f,
            )

    def load(
        self,
        path,
    ):

        with open(path, "rb") as f:
            self.index = pickle.load(f)

        self.retriever = BM25(
            self.index
        )