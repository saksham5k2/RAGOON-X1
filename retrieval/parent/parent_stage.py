from abc import ABC, abstractmethod


class ParentStage(ABC):

    @abstractmethod
    def run(
        self,
        state,
    ):
        pass