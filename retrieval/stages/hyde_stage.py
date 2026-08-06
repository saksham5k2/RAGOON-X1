from retrieval.stages.base import RetrievalStage


class HyDEStage(RetrievalStage):

    def __init__(self, hyde_generator):
        self.hyde_generator = hyde_generator

    def run(self, state):

        hypothetical_document = (
            self.hyde_generator.generate(
                state["rewritten_query"]
            )
        )

        print("\nHyDE Document:")
        print("-" * 80)
        print(hypothetical_document)
        print("-" * 80)

        state["hyde_document"] = hypothetical_document

        return state

