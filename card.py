from dataclasses import dataclass, field, asdict


@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)


if __name__ == "__main__":
    c = Card()
    print(c.to_dict())

    d = {"summary": "esse é o primeiro valor", "owner": "onofre lima", "state": "realizado"}

    dobj = c.from_dict(d)

    print(dobj.to_dict())
