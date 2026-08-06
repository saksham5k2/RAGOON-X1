from openai import OpenAI

from retrieval.hyde.base import BaseHyDEGenerator

from app.settings import (
    GROQ_API_KEY,
    GROQ_BASE_URL,
    LLM_MODEL,
)


class GroqHyDEGenerator(BaseHyDEGenerator):

    def __init__(self):

        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url=GROQ_BASE_URL,
        )

    def generate(
        self,
        query: str,
    ) -> str:

        prompt = f"""
Write a concise factual passage that would likely answer
the following question.

Question:
{query}

Passage:
"""

        response = self.client.chat.completions.create(

            model=LLM_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0,

            max_tokens=200,

        )

        return response.choices[0].message.content.strip()