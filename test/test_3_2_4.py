import pytest 
from src.E_3_2_4 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("24/02/2022",["24","02","2022"])
    ]
)

def test_separarFecha(input_x,expected):
    assert separarFecha(input_x) == expected


@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        (["29","01","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de enero de 2005"),
        (["29","02","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de febrero de 2005"),
        (["29","03","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de marzo de 2005"),
        (["29","04","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de abril de 2005"),
        (["29","05","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de mayo de 2005"),
        (["29","06","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de junio de 2005"),
        (["29","07","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de julio de 2005"),
        (["29","08","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de agosto de 2005"),
        (["29","09","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de septiembre de 2005"),
        (["29","10","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de octubre de 2005"),
        (["29","11","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de noviembre de 2005"),
        (["29","12","2005"],{"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"},"Fecha nuevo formato: 29 de diciembre de 2005")
    ]
)

def test_mensajeSalida(input_x,input_y,expected):
    assert mensajeSalida(input_x,input_y) == expected