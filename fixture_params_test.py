import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    retVal = request.param
    print("\nSetup!   retval = {}".format(retVal))
    return retVal

def test1(setup):
    print("\nSetup = {}".format(setup))
    assert True