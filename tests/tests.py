
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import *

def test_add(): assert add(2,3)==5
def test_subtract(): assert subtract(5,2)==3
def test_multiply(): assert multiply(2,3)==6

def test_divide():
    assert divide(10,2)==5

def test_zero():
    try:
        divide(1,0)
        assert False
    except:
        assert True
