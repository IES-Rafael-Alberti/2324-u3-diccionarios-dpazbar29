import pytest 
from src.E_3_2_9 import * 

'''
def test_gestion(monkeypatch):
    inputs = ["A", "123", "100", "P", "123", "T"]
    expected_output = "Pagado: 100.0\nPendiente pago: 0.0\n"

    def mock_input(_):
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    cobro, pendiente = 0, 0
    assert gestion("A", cobro, pendiente) == (100.0, 100.0)
    assert gestion("P", cobro, pendiente) == (100.0, 0.0)
    assert gestion("T", cobro, pendiente) == (100.0, 0.0)
    assert gestion("T", cobro, pendiente) == (100.0, 0.0)  # Verificar retorno esperado

    monkeypatch.setattr('builtins.input', lambda _: "T")  # Simular finalización
    assert gestion("T", cobro, pendiente) == (100.0, 0.0)
'''
@pytest.mark.parametrize(
        "input_x,input_y,expected",
        [
            (120,120,"Pagado: 120\nPendiente pago: 120")
        ]
)
def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected
