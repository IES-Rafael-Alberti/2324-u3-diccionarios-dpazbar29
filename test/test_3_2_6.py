import pytest
from src.E_3_2_6 import *

def test_datosPersonales(monkeypatch):
    input_values = iter(["nombre", "Daniel", "Si", "apellido", "González", "No"])

    def mock_input(s):
        return next(input_values)

    monkeypatch.setattr("builtins.input", mock_input)

    assert datosPersonales() == {"nombre": "Daniel", "apellido": "González"}