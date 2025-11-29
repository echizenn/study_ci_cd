import pytest

def func():
    return True


def test_pytest():
    assert func() is True

# If you want to demonstrate a failing test, you can uncomment the line below
@pytest.mark.skip(reason="demonstration of skipping")
def test_pytest_ng():
    assert func() is False

# If you want to demonstrate a ruff check failure, you can uncomment the lines below
# def test_ruff_check():
#     var = f"This is a sample string with a trailing whitespace. "
