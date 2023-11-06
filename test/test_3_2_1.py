import pytest 
from src.E_3_2_1 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ({"euro":"€","dollar":"$","yen":"¥"},"euro","La divisa introducida es: €"),
        ({"euro":"€","dollar":"$","yen":"¥"},"dollar","La divisa introducida es: $"),
        ({"euro":"€","dollar":"$","yen":"¥"},"yen","La divisa introducida es: ¥"),
        ({"euro":"€","dollar":"$","yen":"¥"},"aa","La divisa introducida no está registrada")
    ]
)

def test_verificar(input_x,input_y,expected):
    assert verificar(input_x,input_y) == expected