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

        # Number of unique indexed chunks
        self.total_documents = 0

    def add(self, chunks):

        for chunk in chunks:

            chunk_id = chunk.chunk_id

            # ---------------------------------
            # Prevent duplicate document counts
            # ---------------------------------

            is_new = (
                chunk_id
                not in self.documents
            )

            # ---------------------------------
            # Store document
            # ---------------------------------

            self.documents[chunk_id] = chunk

            # ---------------------------------
            # Tokenize
            # ---------------------------------

            tokens = self.tokenizer.tokenize(
                chunk.text
            )

            self.document_lengths[
                chunk_id
            ] = len(tokens)

            # ---------------------------------
            # Update document count
            # ---------------------------------

            if is_new:

                self.total_documents += 1

            # ---------------------------------
            # Calculate term frequencies
            # ---------------------------------

            frequencies = defaultdict(int)

            for token in tokens:

                frequencies[token] += 1

            # ---------------------------------
            # Update inverted index
            # ---------------------------------

            for token, frequency in frequencies.items():

                self.index[token][
                    chunk_id
                ] = frequency

    def lookup(
        self,
        token: str,
    ):

        return self.index.get(
            token,
            {},
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