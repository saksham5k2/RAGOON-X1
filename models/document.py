from dataclasses import dataclass, field


@dataclass
class Document:

    id: str

    title: str

    text: str

    metadata: dict = field(
        default_factory=dict
    )