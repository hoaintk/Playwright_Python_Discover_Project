from dataclasses import dataclass

@dataclass(frozen=True)
class Film:
    name: str
    genre: str
    year: int