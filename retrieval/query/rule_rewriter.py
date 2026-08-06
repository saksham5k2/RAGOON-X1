import re

from retrieval.query.base import BaseQueryRewriter


class RuleQueryRewriter(BaseQueryRewriter):

    def __init__(self):

        self.rules = {

            r"\bai\b":
                "artificial intelligence",

            r"\bml\b":
                "machine learning",

            r"\busa\b":
                "united states",

            r"\buk\b":
                "united kingdom",

            r"\bdb\b":
                "database",

            r"\bcpu\b":
                "central processing unit",

            r"\bgpu\b":
                "graphics processing unit",
        }

    def rewrite(
        self,
        query: str,
    ) -> str:

        rewritten = query.lower()

        for pattern, replacement in self.rules.items():

            rewritten = re.sub(
                pattern,
                replacement,
                rewritten,
            )

        return rewritten