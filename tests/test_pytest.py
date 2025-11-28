def func():
    return True


def test_pytest():
    assert func() is True

def test_pytest_ng():
    assert func() is False