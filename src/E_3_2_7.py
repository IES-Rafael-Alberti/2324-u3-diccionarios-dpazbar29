#3.2.7

def costeCompra(cesta):
    coste = 0
    for producto,precio in cesta.items():
        coste += precio
    return "El precio total es: " + str(coste) + "€"

def precioProducto(cesta):
    
    for producto,precio in cesta.items():
        
        print (producto,"\t",precio)
        #LO SIENTO ❤😕  

if __name__ == "__main__":

    #entrada
    cesta = {}
    continuar = True
    while continuar == True:
        producto = input("Producto a introducir: ")
        precio = round(float(input("Precio de " + str(producto) + ": ")),2)

        cesta[producto] = precio
        continuar = input("¿Quieres seguir añadiendo productos?(Si/No): ") == "Si" 

    #proceso
    coste = costeCompra(cesta)
    producto_precio = precioProducto(cesta)

    #salida
    print(coste)
    print(producto_precio)