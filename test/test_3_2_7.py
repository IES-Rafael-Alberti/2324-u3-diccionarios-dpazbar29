import pytest 
from src.E_3_2_7 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ({"soga":2.50,"banqueta":5.25},"El precio total es: 7.75€")
    ]
)

def test_costeCompra(input_x,expected):
    assert costeCompra(input_x) == expected