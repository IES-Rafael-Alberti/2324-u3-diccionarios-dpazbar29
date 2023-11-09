#3.2.10
clientes = {}
cliente = {}

def menuOpciones():
    return "1.Añadir cliente\n2.Eliminar cliente\n3.Mostrar cliente\n4.Lista clientes\n5.Listar clientes preferentes\n6.Terminar"

def opciones(clientes,cliente,opcion):
    while opcion != "6":
        if opcion == "1":
            nif = input("Introduce el NIF del cliente: ")
            nombre = input("Introduce el nombre del cliente")
            direccion = input("Introduce la dirección del cliente: ")
            telefono = input("Introduce el télefono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            preferencia = input("Cliente preferente o no preferente(S/N): ")
            cliente[nif] = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'correo':correo, 'preferente':preferencia == 'S'}
            clientes[nif] = cliente

        if opcion == "2":
            nif = input("Introduce el NIF del cliente: ")
            if nif in clientes:
                del clientes[nif]
            else:
                return "No existe el cliente con el NIF " + str(nif)
        
        if opcion == "3":
            nif = input("Introduce el NIF del cliente: ")
            if nif in clientes:
                for clave,valor in clientes[nif].items():
                    return str(clave.title()) + ": " + str(valor)
            else:
                return "No hay cliente con el NIF: " + str(nif)
        
        if opcion == "4":
            resultado = []
            for clave,valor in clientes.items():
                resultado.append(clave,valor["nombre"])
                return resultado

        if opcion == "5":
            resultado = []
            for clave,valor in clientes.items():
                if valor["preferente"]:
                    resultado.append(clave,valor["nombre"])
                    return resultado

        opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')

if __name__ == "__main__":
    
    #entrada
    opcion = input("Elija una opción(1-6): ")
    #proceso
    menu = menuOpciones()
    programa = opciones(clientes,cliente,opcion)

    #salida
    print(programa)