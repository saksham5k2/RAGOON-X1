from openai import OpenAI

from generation.base import BaseGenerator


class OpenAIGenerator(BaseGenerator):

    def __init__(
        self,
        model_name: str,
        api_key: str,
        base_url: str,
        temperature: float = 0.0,
        max_tokens: int = 512,
    ):

        self.model_name = model_name

        self.temperature = temperature

        self.max_tokens = max_tokens

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model_name,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=self.temperature,

            max_tokens=self.max_tokens,
        )

        return (
            response
            .choices[0]
            .message
            .content
        )
