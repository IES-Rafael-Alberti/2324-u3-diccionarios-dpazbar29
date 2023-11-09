#3.2.9 

def gestion(opcion):
    facturas = {}
    cobro = 0
    pendiente = 0
    
    while opcion != "T":
        if opcion == "A":
            numero_factura = input("Número de factura: ")
            coste_factura = float(input("Coste de la factura: "))
            
            if coste_factura >= 0:
                facturas[numero_factura] = coste_factura
                pendiente += coste_factura
                print("Estado actual - Cobro: " + str(cobro) + ", Pendiente: " + str(pendiente))
            else:
                while coste_factura <= 0:
                    coste_factura = float(input("Coste de la factura: "))

        if opcion == "P":
            numero_factura = input("Introduce el número de factura a pagar: ")
                
            if numero_factura in facturas:    
                coste_factura = facturas.pop(numero_factura,0)
                cobro += coste_factura
                pendiente -= coste_factura
                print("Estado actual - Cobro: " + str(cobro) + ", Pendiente: " + str(pendiente))
            else:
                print("La factura no existe en la lista de facturas pendientes.")

        opcion = input("¿Añadir nueva factura(A),pagarla(P),terminar(T)?: ").upper()
    return cobro,pendiente

def mensajeSalida(cobro,pendiente):
    return "Pagado: " + str(cobro) + "\nPendiente pago: " + str(pendiente)

if __name__ == "__main__":

    #entrada
    opcion = input("¿Quieres añadir una factura(A) o terminar(T)?: ").upper()

    #proceso
    cobro,pendiente = gestion(opcion)
    mensaje = mensajeSalida(cobro,pendiente)

    #salida
    print(mensaje)