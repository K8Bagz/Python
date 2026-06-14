import pytest

from commands.power import power


def test_power_of_zero():
    assert power(5, 0) == 1


def test_power_of_one():
    assert power(5, 1) == 5

def test_power_of_two():
    assert power(5, 2) == 25


def test_power_negative_exponent():
    with pytest.raises(ValueError):
        power(2, -1)


def test_power_letter():
    with pytest.raises(TypeError):
        power(2, "L")        

# Value error because we do `exponent - 1`.
# At 0.5, it will go to -0.5 and generate Same error as "negative exponent" test.
# TODO improve : stop the recursion when exponent is not an integer.
def test_power_float():
    with pytest.raises(ValueError):
        power(2, 2.5)        
