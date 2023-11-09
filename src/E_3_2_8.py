#3.2.8

def traductor(palabras):

    diccionario = {}

    for i in palabras.split(','):
        palabra_español, palabra_ingles = i.split(':')
        diccionario[palabra_español] = palabra_ingles
    
    return diccionario

def mensajeSalida(diccionario):
    resultado = []

    frase = input("Frase en español: ")

    for i in frase.split():
        if i in diccionario:
            resultado.append(diccionario[i])
        else:
            resultado.append(i)
    
    strResultado = " ".join(resultado)
    return strResultado

if __name__ == "__main__":

    #entrada
    palabras = input("Introduce la palabra y su traducción de la siguiente manera(palabra:traducción,palabra:traducción): ")

    #proceso
    diccionario = traductor(palabras)
    mensaje = mensajeSalida(diccionario)

    #salida
    print(mensaje)

