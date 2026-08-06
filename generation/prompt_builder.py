class PromptBuilder:

    def build(
        self,
        query: str,
        chunks,
    ) -> str:

        context = "\n\n".join(

            chunk.text

            for chunk in chunks

        )

        return f"""
You are a helpful AI assistant.

Use ONLY the provided context.

If the answer cannot be found in the context,
reply exactly:

I don't have enough information to answer that.

--------------------
Context
--------------------

{context}

--------------------
Question
--------------------

{query}

--------------------
Answer
--------------------
""".strip()