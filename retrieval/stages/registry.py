class StageRegistry:

    def __init__(self):
        self._stages = []

    def register(self, stage):
        self._stages.append(stage)

    def get_stages(self):
        return self._stages