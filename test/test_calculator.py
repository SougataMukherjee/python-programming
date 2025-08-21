import pytest
from python.calculator import greet, add, subtract

def test_greet():
    assert greet("Sam") == "Hello, Sam!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
