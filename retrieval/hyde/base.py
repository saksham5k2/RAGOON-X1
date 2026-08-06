from abc import ABC, abstractmethod


class BaseHyDEGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        query: str,
    ) -> str:
        pass