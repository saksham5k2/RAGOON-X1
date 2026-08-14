from abc import ABC, abstractmethod

from models.document import Document


class BaseDocumentLoader(ABC):

    @abstractmethod
    def load(self):
        pass