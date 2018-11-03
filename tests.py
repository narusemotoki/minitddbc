import semver


def test_文字列表現():
    assert str(semver.Semver("1", "4", "2")) == "1.4.2"
