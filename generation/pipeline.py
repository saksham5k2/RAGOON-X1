from generation.factory import GeneratorFactory
from generation.prompt_builder import PromptBuilder
from generation.response import GeneratedResponse


class GenerationPipeline:

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        self.generator = (
            GeneratorFactory.create()
        )

    def generate(
        self,
        query,
        chunks,
    ):

        prompt = self.prompt_builder.build(
            query,
            chunks,
        )

        answer = self.generator.generate(
            prompt
        )

        return GeneratedResponse(
            answer=answer,
            prompt=prompt,
            sources=chunks,
        )