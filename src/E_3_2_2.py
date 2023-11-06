#3.2.2

def mensajeSalida(informacion):
    return str(informacion["nombre"]) + " tiene " + str(informacion["edad"]) + " años, vive en " + str(informacion["direccion"]) + " y su número de teléfono es " + str(informacion["telefono"])

if __name__ == "__main__":

    #entrada
    informacion = {"nombre":input("Introduzca su nombre: "),"edad":input("Introduzca su edad: "),"direccion":input("Introduzca su dirección: "),"telefono":input("Introduzca su teléfono: ")}

    #proceso
    mensaje = mensajeSalida(informacion)

    #salida
    print(mensaje)