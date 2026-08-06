from retrieval.hyde.generator import (
    GroqHyDEGenerator,
)


class HyDEFactory:

    @staticmethod
    def create():

        return GroqHyDEGenerator()