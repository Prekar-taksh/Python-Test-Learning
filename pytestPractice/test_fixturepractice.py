import pytest

@pytest.fixture
def x():
    return 5

def test_file1_method1(x):
    y = 6
    assert x + 1 == y, "test passed"
