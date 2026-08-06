from abc import ABC, abstractmethod

from chunking.chunk import Chunk

from abc import ABC, abstractmethod

class BaseVectorStore(ABC):

    @abstractmethod
    def create_collection(self):
        pass

    @abstractmethod
    def add(self, chunks):
        pass

    @abstractmethod
    def search(self, embedding, limit=10):
        pass

    @abstractmethod
    def close(self):
        pass

class BaseVectorStore(ABC):

    @abstractmethod
    def create_collection(self):
        """Create the collection if it doesn't exist."""
        pass

    @abstractmethod
    def add(self, chunks: list[Chunk]):
        """Store chunks."""
        pass

    @abstractmethod
    def search(self, embedding: list[float], limit: int = 10):
        """Search for similar vectors."""
        pass

    @abstractmethod
    def close(self):
        pass