import pytest 
from src.E_3_2_2 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ({"nombre":"Jose","edad":"13","direccion":"C/ABC","telefono":"123 456 789"},"Jose tiene 13 años, vive en C/ABC y su número de teléfono es 123 456 789")
    ]
)

def test_mensajeSalida(input_x,expected):
    assert mensajeSalida(input_x) == expected