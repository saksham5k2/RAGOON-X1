from dataclasses import dataclass


@dataclass
class GeneratedResponse:

    answer: str

    prompt: str

    sources: list