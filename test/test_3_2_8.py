import pytest 
from src.E_3_2_8 import *


@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("hola:hello,madre:mother",{"hola":"hello","madre":"mother"})
    ]
)

def test_traductor(input_x,expected):
    assert traductor(input_x) == expected 


def test_mensajeSalida(monkeypatch):
    diccionario = {"hola":"hello","madre":"mother"}
    input_values = "hola madre"
    def mock_input(s):
        return input_values
    monkeypatch.setattr("builtins.input",mock_input)
    assert mensajeSalida(diccionario) == "hello mother"