# https://docs.pytest.org/en/8.2.x/how-to/usage.html#
# 'pytest src_tests.py'
from pytest import *
import src as src

def setup():
    return 'setup'

def teardown():
    return 'teardown'

def test_basic():
    assert setup() == "setup"
def test_2():
    assert teardown() == "teardown"