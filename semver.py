from typing import (
    Any,
    NamedTuple,
)


class Semver(NamedTuple):
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @classmethod
    def _validate(cls, version: Any) -> None:
        if not isinstance(version, int):
            raise TypeError("Version must be integer.")

        if version < 0:
            raise ValueError("Version must be positive integer or 0.")

    @classmethod
    def create(cls, major: int, minor: int, patch: int) -> 'Semver':
        for version in [major, minor, patch]:
            cls._validate(version)

        return cls(major, minor, patch)
