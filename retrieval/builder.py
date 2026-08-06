from retrieval.stages.registry import StageRegistry


class RetrievalPipelineBuilder:

    def __init__(self):

        self.registry = StageRegistry()

    def add_stage(
        self,
        stage,
    ):

        self.registry.register(stage)

        return self

    def build(self):

        return self.registry.get_stages()