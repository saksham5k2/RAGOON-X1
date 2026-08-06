from app.settings import (
    LLM_PROVIDER,
    LLM_MODEL,
)

from generation.openai_generator import (
    OpenAIGenerator,
)


class GeneratorFactory:

    @staticmethod
    def create():

        provider = LLM_PROVIDER.lower()

        if provider == "groq":

            return OpenAIGenerator(
                LLM_MODEL
            )

        raise ValueError(
            f"Unsupported provider: {provider}"
        )