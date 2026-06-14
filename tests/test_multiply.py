import pytest

from commands.multiply import multiply


def test_multiply_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(5, -1) == -5

def test_multiply_positive():
    assert multiply(5, 2) == 10

def test_multiply_float():
     assert multiply(2, 2.5) == 5   

#TODO improve : prevent input of letters
def test_multiply_letter():
    assert multiply(2, "L")  == "LL"    

            