import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")
    yield
    print("\nTeardown")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True
