import pytest 
from src.E_3_2_1 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("euro",True)
    ]
)

def test_Divisa(input_x,expected):
    assert Divisa(input_x) == expected