from retrieval.stages.base import RetrievalStage


class PostProcessingStage(RetrievalStage):

    def run(self, state):

        return state["compressed"]