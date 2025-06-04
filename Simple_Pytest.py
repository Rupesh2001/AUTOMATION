import pytest

@pytest.fixture
def SetUp():
    print("\tDriver setup")
    yield SetUp
    print("\tAfter Yield")

def test_first(SetUp):
    print("\tThis is the first test")

def test_second(SetUp):
    print("\tThis is the second test")
