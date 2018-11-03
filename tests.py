import semver

import pytest


@pytest.mark.parametrize("source,expect", [
    ((1, 4, 2), "1.4.2"),
    ((2, 1, 1), "2.1.1"),
])
def test_文字列表現(source, expect):
    assert str(semver.Semver.create(*source)) == expect


@pytest.mark.parametrize("source,other,expect", [
    ((1, 4, 2),(1, 4, 2), True),
    ((2, 1, 1),(3, 5, 4), False),
])
def test_バージョン比較(source, other, expect):
    assert (semver.Semver.create(*source) == semver.Semver.create(*other)) == expect
