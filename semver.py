from typing import NamedTuple


class Semver(NamedTuple):
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @classmethod
    def create(cls, major, minor, patch):
        if not isinstance(major, int):
            raise TypeError()

        if not isinstance(minor, int):
            raise TypeError()

        if not isinstance(patch, int):
            raise TypeError()

        return cls(major, minor, patch)
