#3.2.3
def precioFinal(precios,fruta_usuario,kilos_usuario):
    if fruta_usuario in precios:
        precio = round(precios[fruta_usuario] * kilos_usuario,2)
    else:
        precio = "La fruta no está registrada"
    return precio

def mensajeSalida(precios,fruta_usuario,precio_final):
    if fruta_usuario in precios:
        mensaje = "El precio final es: " + str(precio_final)
    else:
        mensaje = precio_final
    return mensaje
if __name__ == "__main__":

    #entrada
    precios = {"plátano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
    fruta_usuario = input("Introduzca la fruta que desee: ").lower()
    kilos_usuario = int(input("Introduzca la cantidad de la fruta pedida: "))

    #proceso
    precio_final = precioFinal(precios,fruta_usuario,kilos_usuario)
    mensaje_salida = mensajeSalida(precios,fruta_usuario,precio_final)

    #salida
    print(mensaje_salida)