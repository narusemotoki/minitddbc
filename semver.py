from typing import NamedTuple


class Semver(NamedTuple):
    major: str
    minor: str
    patch: str

    def __str__(self) -> str:
        return ".".join(self)
