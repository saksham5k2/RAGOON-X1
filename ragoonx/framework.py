from config.loader import ConfigLoader

from rag.pipeline import RagPipeline


class Framework:

    def __init__(
        self,
        config_path="ragoonx.yaml",
    ):

        self.config = ConfigLoader.load(
            config_path
        )

        self.pipeline = RagPipeline(
            self.config
        )

    def answer(
        self,
        query,
    ):

        return self.pipeline.answer(
            query
        )

    def close(self):

        self.pipeline.close()