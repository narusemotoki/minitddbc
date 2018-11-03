from typing import (
    Any,
    NamedTuple,
)


class Semver(NamedTuple):
    """プロフェッショナルユーザ以外はコンストラクタ式を呼ばないでください。
    代わりにcreateを呼んでください。
    """
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @classmethod
    def _validate(cls, version: Any) -> None:
        """バージョンが許されない値であればエラーを上げます。

        :raise TypeError: versionがint型でなかった場合
        :raise ValueError: versionが負の値の場合
        """
        if not isinstance(version, int):
            raise TypeError("Version must be integer.")

        if version < 0:
            raise ValueError("Version must be positive integer or 0.")

    @classmethod
    def create(cls, major: int, minor: int, patch: int) -> "Semver":
        """インスタンスを作るためのメソッドです。

        コンストラクタ式の代わりに呼んでください。コンストラクタ式との違いは、
        値のバリデーションがこちらにあることです。
        """
        for version in [major, minor, patch]:
            cls._validate(version)

        return cls(major, minor, patch)

    def bump_patch(self) -> "Semver":
        """パッチバージョンを上げた新しいインスタンスを返します。
        """
        return self._replace(patch=self.patch+1)

    def bump_minor(self) -> "Semver":
        """マイナーバージョンを上げた新しいインスタンスを返します。

        マイナーバージョンが上がるときには、パッチは0に戻ります。
        """
        return self._replace(minor=self.minor+1, patch=0)

    def bump_major(self) -> "Semver":
        """メジャーバージョンを上げた新しいインスタンスを返します。

        メジャーバージョンが上がるときには、マイナーおよびパッチは0に戻ります。
        """
        return self._replace(major=self.major+1, minor=0, patch=0)
