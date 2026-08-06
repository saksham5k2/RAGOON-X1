from abc import ABC, abstractmethod


class RetrievalStage(ABC):

    @abstractmethod
    def run(self, data):
        pass