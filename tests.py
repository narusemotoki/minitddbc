import semver

import pytest


@pytest.mark.parametrize("source,expect", [
    (("1", "4", "2"), "1.4.2"),
    (("2", "1", "1"), "2.1.1"),
])
def test_文字列表現(source, expect):
    assert str(semver.Semver(*source)) == expect
