#3.2.11

def gestionDirectorio(datos_clientes):
    '''separa los campos dados y los ordena en su posicion'''
    lista_clientes = datos_clientes.split('\n')
    directorio = {}
    lista_campos = lista_clientes[0].split(';') 
    for i in lista_clientes[1:]:
        cliente = {}
        lista_info = i.split(';') 
        for j in range(1,len(lista_campos)):
            if lista_campos[j] == 'descuento':
                lista_info[j] = float(lista_info[j])
            cliente[lista_campos[j]] = lista_info[j]
        directorio[lista_info[0]] = cliente
    return directorio


if __name__ == "__main__":

    #entrada
    datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7" 
    #proceso

    #salida