from retrieval.fusion.rrf import (
    ReciprocalRankFusion,
)


class FusionFactory:

    @staticmethod
    def create():

        return ReciprocalRankFusion()