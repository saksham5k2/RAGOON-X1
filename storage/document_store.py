from abc import ABC, abstractmethod


class BaseDocumentStore(ABC):

    @abstractmethod
    def add(self, document):
        pass

    @abstractmethod
    def get(self, document_id):
        pass

    @abstractmethod
    def close(self):
        pass