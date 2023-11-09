import pytest 
from src.E_3_2_9 import * 


def test_gestion(monkeypatch):
    inputs = ["A", "123", "100", "P", "123", "T"]
    def mock_input(s):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert gestion(["A", "123", "100", "P", "123", "T"]) == (100.0, 0)

@pytest.mark.parametrize(
        "input_x,input_y,expected",
        [
            (120,120,"Pagado: 120\nPendiente pago: 120")
        ]
)
def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected
