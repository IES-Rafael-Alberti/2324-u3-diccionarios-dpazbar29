#3.2.1



def verificar(divisas,divisa_usuario):
    divisa_usuario.lower()

    if divisa_usuario in divisas:
        mensaje = "La divisa introducida es: " + str(divisas[divisa_usuario])
    else: 
        mensaje = "La divisa introducida no está registrada"
    
    return mensaje
 

if __name__ == "__main__":

    #entrada
    divisas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
    divisa_usuario = str(input("Introduzca una divisa: "))

    #proceso
    verif = verificar(divisas,divisa_usuario)
    
    #salida
    print(verif)
    