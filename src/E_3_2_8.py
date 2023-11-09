#3.2.8

def diccionario(palabras):

    diccionario = {}

    for i in palabras.split(','):
        palabra_español, palabra_ingles = i.split(':')
        diccionario[palabra_español] = palabra_ingles
    
    return diccionario

def traductor(diccionario):
    resultado = []

    frase = input("Frase en español: ")

    for i in frase.split():
        if i in diccionario:
            resultado.append(diccionario[i])
        else:
            resultado.append(i)
    
    strResultado = " ".join(resultado)
    return frase , strResultado

def mensajeSalida(frase,strResultado):
    return "La frase en español: " + str(frase) + "\nLa frase traducida al inglés: " + str(strResultado)
if __name__ == "__main__":

    #entrada
    palabras = input("Introduce la palabra y su traducción de la siguiente manera(palabra:traducción,palabra:traducción): ")

    #proceso
    dic = diccionario(palabras)
    frase , strResultado = traductor(dic)
    mensaje = (mensajeSalida(frase , strResultado))

    #salida
    print(mensaje)

