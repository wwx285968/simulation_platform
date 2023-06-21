from dataclasses import asdict, dataclass


@dataclass
class Entity:
    def dict(self):
        return asdict(self)
