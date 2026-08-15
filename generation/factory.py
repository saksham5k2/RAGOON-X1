from generation.openai_generator import (
    OpenAIGenerator,
)


class GeneratorFactory:

    @staticmethod
    def create(
        llm_config,
    ):

        provider = (
            llm_config.provider.lower()
        )

        if provider == "groq":

            return OpenAIGenerator(

                model_name=llm_config.model,

                api_key=llm_config.api_key,

                base_url=llm_config.base_url,

                temperature=llm_config.temperature,

                max_tokens=llm_config.max_tokens,
            )

        raise ValueError(
            f"Unsupported provider: {provider}"
        )