import pytest 
from src.E_3_2_5 import * 


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5},15)
    ]
)

def test_calculoCreditos(input_x,expected):
    assert calculoCreditos(input_x) == expected


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ({'Matemáticas': 6, 'Física': 4, 'Química': 5},["Matemáticas tiene 6 créditos","Física tiene 4 créditos","Química tiene 5 créditos"])
    ]
)

def test_estructura(input_x,expected):
    assert estructura(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (["Matemáticas tiene 6 créditos","Física tiene 4 créditos","Química tiene 5 créditos"],15,"Matemáticas tiene 6 créditos\nFísica tiene 4 créditos\nQuímica tiene 5 créditos\nLos créditos totales son 15")
    ]
)

def test_(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected