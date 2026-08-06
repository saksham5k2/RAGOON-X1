from abc import ABC, abstractmethod


class BaseQueryRewriter(ABC):

    @abstractmethod
    def rewrite(
        self,
        query: str,
    ) -> str:
        pass