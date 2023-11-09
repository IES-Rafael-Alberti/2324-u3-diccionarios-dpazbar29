import pytest 
from src.E_3_2_8 import *


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("hola:hello,madre:mother",{"hola":"hello","madre":"mother"})
    ]
)

def test_diccionario(input_x,expected):
    assert diccionario(input_x) == expected 


def test_traductor(monkeypatch):
    diccionario = {"hola":"hello","madre":"mother"}
    input_values = "hola madre"
    def mock_input(s):
        return input_values
    monkeypatch.setattr("builtins.input",mock_input)
    assert traductor(diccionario) == ('hola madre', 'hello mother')


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ('hola madre', 'hello mother',"La frase en español: hola madre\nLa frase traducida al inglés: hello mother")
    ]
)

def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected