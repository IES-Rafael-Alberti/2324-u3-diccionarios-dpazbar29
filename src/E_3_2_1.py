#3.2.1

def Divisa(divisas):
    divisa_usuario.lower()

    if divisa_usuario in divisas:
        return True
    else:
        return False

def verificarSi(divisas,divisa_usuario,entrada):
    resultado = "".join(divisas[divisa_usuario])
    if entrada == True:
        return "El simbolo de " + str(divisa_usuario) + " es: " + str(resultado)

def verificarNo(entrada):
    if entrada == False:
        return "Esa divisa no está en el diccionario"

if __name__ == "__main__":

    #entrada
    divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
    divisa_usuario = input("introduzca una divisa: ")

    #proceso
    entrada = Divisa(divisa_usuario)
    verif_si = verificarSi(divisas,divisa_usuario,entrada)
    verif_no = verificarNo(entrada)

    #salida
    if entrada == True:
        print(verif_si)
    else:
        print(verif_no)