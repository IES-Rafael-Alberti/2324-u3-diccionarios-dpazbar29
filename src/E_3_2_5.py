#3.2.5

def calculoCreditos(asign):

    creditos_finales = 0
    
    for asignatura,creditos in asign.items():
        creditos_finales += creditos
    return creditos_finales

def estructura(asign):

    mensaje = []

    for asignatura,creditos in asign.items():
        mensaje.append(str(asignatura) + " tiene " + str(creditos) + " créditos")
    return mensaje

def mensajeSalida(estruct,creditos_fin):
    strMensaje = "\n".join(estruct)      
    
    return str(strMensaje) + "\nLos créditos totales son " + str(creditos_fin) 
if __name__ == "__main__":

    #entrada
    asign = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    #proceso
    creditos_fin = calculoCreditos(asign)
    estruct = estructura(asign)
    mensaje_salida = mensajeSalida(estruct,creditos_fin)

    #salida
    print(mensaje_salida)