from collections import defaultdict

from retrieval.sparse.tokenizer import Tokenizer


class InvertedIndex:

    def __init__(self):

        self.tokenizer = Tokenizer()

        # term -> {chunk_id: frequency}
        self.index = defaultdict(dict)

        # chunk_id -> Chunk
        self.documents = {}

        # chunk_id -> document length
        self.document_lengths = {}

        self.total_documents = 0

    def add(self, chunks):

        for chunk in chunks:

            self.documents[chunk.chunk_id] = chunk

            tokens = self.tokenizer.tokenize(
                chunk.text
            )

            self.document_lengths[
                chunk.chunk_id
            ] = len(tokens)

            self.total_documents += 1

            frequencies = defaultdict(int)

            for token in tokens:
                frequencies[token] += 1

            for token, frequency in frequencies.items():

                self.index[token][
                    chunk.chunk_id
                ] = frequency

    def lookup(self, token: str):

        return self.index.get(
            token,
            {}
        )

    def document_frequency(
        self,
        token: str,
    ):

        return len(
            self.lookup(token)
        )

    def average_document_length(self):

        if self.total_documents == 0:
            return 0

        return (
            sum(
                self.document_lengths.values()
            )
            / self.total_documents
        )