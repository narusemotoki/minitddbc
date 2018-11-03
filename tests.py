import semver

import pytest


@pytest.mark.parametrize("source,expect", [
    ((1, 4, 2), "1.4.2"),
    ((2, 1, 0), "2.1.0"),
])
def test_文字列表現(source, expect):
    assert str(semver.Semver.create(*source)) == expect


@pytest.mark.parametrize("source,other,expect", [
    ((1, 4, 2), (1, 4, 2), True),
    ((2, 1, 1), (3, 5, 4), False),
])
def test_バージョン比較(source, other, expect):
    assert (semver.Semver.create(*source) == semver.Semver.create(*other)) \
        == expect


@pytest.mark.parametrize("source", [
    (-1, 4, 2),
    (2, -1, 1),
    (2, 1, -1),
])
def test_負の数だったらエラー(source):
    with pytest.raises(ValueError):
        semver.Semver.create(*source)


@pytest.mark.parametrize("source", [
    (1, "4", 2),
    (2, 1, "1"),
    ("2", 1, 1),
    ("True", "a", "bc"),
])
def test_文字列が来たらエラー(source):
    with pytest.raises(TypeError):
        semver.Semver.create(*source)


@pytest.mark.parametrize("source, expect", [
    ((1, 1, 0), (1, 1, 1))
])
def test_パッチを上げるテスト(source, expect):
    before = semver.Semver.create(*source)
    assert before.bump_patch() == semver.Semver.create(*expect)


@pytest.mark.parametrize("source, expect", [
    ((1, 1, 1), (1, 2, 0)),
    ((0, 9, 0), (0, 10, 0)),
])
def test_マイナーを上げるテスト(source, expect):
    before = semver.Semver.create(*source)
    assert before.bump_minor() == semver.Semver.create(*expect)


@pytest.mark.parametrize("source, expect", [
    ((1, 0, 0), (2, 0, 0)),
    ((0, 9, 0), (1, 0, 0)),
    ((9, 9, 5), (10, 0, 0)),
])
def test_メジャーを上げるテスト(source, expect):
    before = semver.Semver.create(*source)
    assert before.bump_major() == semver.Semver.create(*expect)

