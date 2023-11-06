#3.2.4

def separarFecha(fecha):
    fecha = fecha.split("/")
    return fecha

def mensajeSalida(fecha_separada,meses):
    return "Fecha nuevo formato: " + str(fecha_separada[0]) + " de " + str(meses[fecha_separada[1]]) + " de " + str(fecha_separada[2])
if __name__ == "__main__": 

    #entrada
    fecha = input("Introduce una fecha(dd/mm/aaaa): ")
    meses = {"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"}

    #proceso
    fecha_separada = separarFecha(fecha)
    mensaje_salida = mensajeSalida(fecha_separada,meses)

    #salida
    print(mensaje_salida)