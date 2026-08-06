from openai import OpenAI

from generation.base import BaseGenerator

from app.settings import (
    GROQ_API_KEY,
    GROQ_BASE_URL,
)


class OpenAIGenerator(BaseGenerator):

    def __init__(
        self,
        model_name: str,
    ):

        self.model_name = model_name

        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url=GROQ_BASE_URL,
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

            temperature=0,

            max_tokens=512,

        )

        return response.choices[0].message.content