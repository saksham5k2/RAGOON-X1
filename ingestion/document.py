from dataclasses import dataclass, field

@dataclass
class Document:
    id: str
    title: str
    text: str
    source: str
    metadata: dict = field(default_factory=dict)