from retrieval.query.rule_rewriter import RuleQueryRewriter


class QueryRewriterFactory:

    @staticmethod
    def create():

        return RuleQueryRewriter()