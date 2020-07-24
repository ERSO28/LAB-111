import os


def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def titulo():
    print("PRACTICA---PROCESOS BANCARIOS---")


def menu():
    print("""   
    1. Registra cliente.
    2. Editar informacion del Cliente.
    3. Habilitar o inhabilitar.
    4. Mostrar clientes habilitados.
    5. Mostrat cliente inhabilitados.
    6. Depositar o retirar monto.
    7. Calcular millas.
    8. Probabilidad de X cliente.
    9. Converion a diferentes tipos de cambio.
    0. Salir
    """)


def registrar_cliente():
    cliente_estado.append(True)
    cliente_nombre.append(input('Ingrese el nombre del nuevo cliente:\n'))
    cliente_apellido.append(input('Ingrese el apellido del nuevo cliente:\n'))
    cliente_carnet.append(input('Ingrese el carnet de identidad del nuevo cliente:\n'))
    cliente_residencia.append(input('Ingrese el lugar de residencia del nuevo cliente:\n'))
    cliente_monto_bolivianos.append(
        int(input('Ingrese el monto en bolivianos con el cuál el cliente aperturará la cuenta:\n')))
    cliente_monto_dolares.append(
        int(input('Ingrese el monto en dolares con el cuál el cliente aperturará la cuenta:\n')))
    limpiar_consola()
    print('Cliente registrado con exito.')


def editar_informacion():
    cliente_carnet_aux = input('Ingrese el carnet del cliente a modificar')
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = cliente_carnet.index(cliente_carnet_aux)
            cliente_residencia[indice] = input('Ingrese la residencia corregida: ')
            cliente_monto_bolivianos[indice] = int(input('Ingrese el monto corregido: '))
            limpiar_consola()
            print('Se corrigieron los datos.')
            break
        else:
            limpiar_consola()
            cliente_carnet_aux = input("El carnet que ingreso no existe.\nVuelva a ingresarlo: ")


def cambiar_estado_cliente():
    cliente_carnet_aux = input('Ingrese el carnet del cliente a habilitar o inhabilitar: ')
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = cliente_carnet.index(cliente_carnet_aux)
            if cliente_estado == 'Habilitado':
                usuario_opcion_hab = input('El cliente se encuentra habilitado. Desea inhabilitarlo?.(s/n): ').lower()
                if usuario_opcion_hab == 's':
                    cliente_estado[indice] = 'Inhabilitado'
                    limpiar_consola()
                    print('Cambio de estado exitoso.')
                    break
            else:
                usuario_opcion_hab = input('El cliente se encuentra inhabilitado. Desea habilitarlo?.(s/n): ').lower()
                if usuario_opcion_hab == 's':
                    cliente_estado[indice] = 'Habilitado'
                    limpiar_consola()
                    print('Cambio de estado exitoso.')
                    break


def mostrar_clientes_hab():
    for i in range(len(cliente_estado)):
        if cliente_estado[i] == 'Habilitado':
            print(cliente_nombre[i], cliente_apellido[i], cliente_carnet[i], cliente_residencia[i])


def mostrar_clientes_inhab():
    for i in range(len(cliente_estado)):
        if cliente_estado[i] != 'Habilitado':
            print(cliente_nombre[i], cliente_apellido[i], cliente_carnet[i], cliente_residencia[i])


def cambios_monto():
    cliente_carnet_aux = input('Ingrese el carnet del cliente a modificar: ')
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = cliente_carnet.index(cliente_carnet_aux)
            print('El saldo del cliente es de', cliente_monto_bolivianos[indice], ' Bolivianos'
                                              , cliente_monto_dolares[indice], 'Dolares')
            usuario_opcion_monto = input("""Que desea realizar:\n1. Retirar\n2. Depositar\n3. Salir""")
            if usuario_opcion_monto == '1':
                usuario_opcion_monto = input(""""Escoja el tipo de cambio que utilizara:\n1. Bolivianos\n2. Dolares\n3. Salir\n""")
                if usuario_opcion_monto == '1':
                    monto_aux = int(input('Ingrese el monto a retirar: '))
                    cliente_monto_bolivianos[indice] = cliente_monto_bolivianos[indice] - monto_aux
                elif usuario_opcion_monto == '2':
                    monto_aux = int(input('Ingrese el monto a retirar: '))
                    cliente_monto_dolares[indice] = cliente_monto_dolares[indice] - monto_aux
                elif usuario_opcion_monto == '3':
                    break
                else:
                    usuario_opcion_monto = input('La opcion que ingreso es invalida. Vuelva a intentar')
            elif usuario_opcion_monto == '2':
                usuario_opcion_monto = input("""Escoja el tipo de cambio que utilizara:\n1. Bolivianos\n2. Dolares\n3. Salir""")
                if usuario_opcion_monto == '1':
                    monto_aux = int(input('Ingrese el monto a depositar: '))
                    cliente_monto_bolivianos[indice] = cliente_monto_bolivianos[indice] + monto_aux
                    limpiar_consola()
                    print("El monto total es: ", cliente_monto_bolivianos[indice])
                    break
                elif usuario_opcion_monto == '2':
                    monto_aux = int(input('Ingrese el monto a depositar: '))
                    cliente_monto_dolares[indice] = cliente_monto_dolares[indice] + monto_aux
                    limpiar_consola()
                    print('El monto total es: ', cliente_monto_dolares[indice])
                    break
                elif usuario_opcion_monto == '3':
                    break
            elif usuario_opcion_monto == '3':
                break
            else:
                usuario_opcion_monto = input('La opcion que ingreso es invalida. Vuelva a intentar')
        else:
            cliente_carnet_aux = input('El carnet que ingreso no existe. Vuelva a intentar.')


def calcular_millas():
    cliente_carnet_aux = input('Introduzca el carnet del cliente a calcular: ')
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = cliente_carnet.index(cliente_carnet_aux)
            variable = float(input('Ingrese un numero entre 0 y 1: '))
            while True:
                if 0 < variable < 1:
                    limpiar_consola()
                    print("La cantidad de millas que tiene ahorrado es: ", cliente_monto_dolares[indice] * variable)
                    break
                else:
                    variable = float(input('Opcion no valida. Intente de nuevo'))
        else:
            cliente_carnet_aux = input('Opcion invalida. Intente de nuevo: ')


def calcular_probabilidades():
    cliente_carnet_aux = input('Ingrese el carnet de identidad del cliente:')
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = len(cliente_monto_bolivianos)
            indice_2 = cliente_carnet.index(cliente_carnet_aux)
            nombre = cliente_nombre[indice_2]
            apellido = cliente_apellido[indice_2]
            lista_contadores = []
            contador = 0
            for i in range(indice):
                cliente_monto_bolivianos_aux = cliente_monto_bolivianos[i]
                print(i)
                while cliente_monto_bolivianos_aux > 1:
                    contador += 1
                    cliente_monto_bolivianos_aux = cliente_monto_bolivianos_aux // 100
                lista_contadores.append(contador)
            total = sum(lista_contadores)
            probabilidad = (lista_contadores[indice_2] / total) * 100
            limpiar_consola()
            print('La probabilidad del cliente ', nombre, apellido, ' es ', probabilidad, '%')
            break


def conversion_tipo():
    cliente_carnet_aux = input('Ingrese un carnet de identidad: ')
    tipo_dolares_bolivianos = 6.90
    tipo_bolivianos_dolares = 0.14
    tipo_bolivianos_euros = 0.12
    tipo_dolares_euros = 0.86
    while True:
        if cliente_carnet_aux in cliente_carnet:
            indice = cliente_carnet.index(cliente_carnet_aux)
            usuario_opcion_aux = input("""  Escoja el tipo de cambio que desea realizar: 
                                                1. Dolares a bolivianos.
                                                2. Bolivianos a dolares.
                                                3. Dolares a Euros
                                                4. Bolivianos a euros.
                                                5. Salir""")
            if usuario_opcion_aux == '1':
                conversion = cliente_monto_dolares[indice] * tipo_dolares_bolivianos
                limpiar_consola()
                print('El valor de la conversion es: ', conversion)
                break
            elif usuario_opcion_aux == '2':
                limpiar_consola()
                conversion = cliente_monto_bolivianos[indice] * tipo_bolivianos_dolares
                print('El valor de la conversion es: ', conversion)
                break
            elif usuario_opcion_aux == '3':
                limpiar_consola()
                conversion = cliente_monto_dolares[indice] * tipo_dolares_euros
                print('El valor de la conversion es: ', conversion)
                break
            elif usuario_opcion_aux == '4':
                limpiar_consola()
                conversion = cliente_monto_bolivianos[indice] * tipo_bolivianos_euros
                print('El valor de la conversion es: ', conversion)
                break
            elif usuario_opcion_aux == '5':
                break
            else:
                usuario_opcion_aux = input('Opcion invalida. Intente otra vez: ')
        else:
            cliente_carnet_aux = input('No existe. Pruebe con otro: ')


cliente_estado = ['Habilitado', 'Inhabilitado']
cliente_nombre = ['Juan', 'Alejandro']
cliente_apellido = ['Rivera', 'Valencia']
cliente_carnet = ['123', '456']
cliente_residencia = ['La Paz', 'Oruro']
cliente_monto_bolivianos = [100, 900]
cliente_monto_dolares = [900, 100]


while True:
    titulo()
    menu()
    usuario_opcion = input('Introduzca la opcion que desea realizar: ')
    if usuario_opcion == '1':
        registrar_cliente()
    elif usuario_opcion == '2':
        editar_informacion()
    elif usuario_opcion == '3':
        cambiar_estado_cliente()
    elif usuario_opcion == '4':
        mostrar_clientes_hab()
    elif usuario_opcion == '5':
        mostrar_clientes_inhab()
    elif usuario_opcion == '6':
        cambios_monto()
    elif usuario_opcion == '7':
        calcular_millas()
    elif usuario_opcion == '8':
        calcular_probabilidades()
    elif usuario_opcion == '9':
        conversion_tipo()
    elif usuario_opcion == '0':
        break
    else:
        usuario_opcion = input('Opcion no valida. Intente otra vez: ')
