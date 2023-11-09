#3.2.6

def datosPersonales():
    informacion = {}
    continuar = True
    while continuar == True:
        clave = input("Campo a introducir: ")
        valor = input("Rellena el campo " + str(clave) + ": ")

        informacion[clave] = valor
        continuar = input("¿Quieres seguir añadiendo infomración?(Si/No): ") == "Si" 
    return informacion
if __name__ == "__main__":

    #entrada
    entrada = datosPersonales()

    #proceso
    

    #salida
    print(entrada)