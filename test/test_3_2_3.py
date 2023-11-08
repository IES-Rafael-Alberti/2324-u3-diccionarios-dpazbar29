import pytest 
from src.E_3_2_3 import *

@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"manzana",2,1.6),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"plátano",2,2.7),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"pera",2,1.7),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"naranja",2,1.4),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"a",2,"La fruta no está registrada")

    ]
)

def test_precioFinal(input_x,input_y,input_z,expected):
    assert precioFinal(input_x,input_y,input_z) == expected


@pytest.mark.parametrize(
    "input_x,input_y,input_z,expected",
    [
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"manzana",1.6,"El precio final es: 1.6"),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"plátano",2.7,"El precio final es: 2.7"),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"pera",1.7,"El precio final es: 1.7"),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"naranja",1.4,"El precio final es: 1.4"),
        ({"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70},"a","La fruta no está registrada","La fruta no está registrada")
    ]
)

def test_mensajeSalida(input_x,input_y,input_z,expected):
    assert mensajeSalida(input_x,input_y,input_z) == expected