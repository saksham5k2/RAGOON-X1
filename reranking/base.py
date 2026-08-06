from abc import ABC, abstractmethod

class BaseReranker(ABC):

    @abstractmethod
    def rerank(
        self,
        query: str,
        results,
        top_k: int,
    ):
        pass