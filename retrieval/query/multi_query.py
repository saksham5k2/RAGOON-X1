class MultiQueryGenerator:

    def generate(
        self,
        query: str,
    ) -> list[str]:

        query = query.strip()

        queries = {query}

        # Remove question mark
        queries.add(query.replace("?", ""))

        # Add "what is"
        queries.add(f"What is {query}")

        # Add definition form
        queries.add(f"{query} definition")

        return list(queries)