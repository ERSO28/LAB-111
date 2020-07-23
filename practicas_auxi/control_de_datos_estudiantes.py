#Editado por: Rivera Valencia Juan Alejandro

import os
from datetime import datetime

estudiantes_nombres = ['Arun', 'Daniel']
estudiantes_apellidos = ['Limachi', 'Rivera']
estudiantes_CI = ['8463443', '2']
estudiantes_fecha = [1994, 2000]
estudiantes_telefono = ['71201944', '72002015']


def mostrar_menu():
    print("\033[;36m"+"CONTROL DE DATOS DE ESTUDIANTES")
    print()
    print('Ingrese la opcion requerida: ')
    print('1. Mostrar la lista')
    print('2. Adicionar un estudiante')
    print('3. Modificar un estudiante')
    print('4. Eliminar un estudiante')
    print('5. Consulta Salida cuarentena')
    print('6. Consultar la edad')
    print('0. Salir')
    print('')


def mostrar_estudiantes():
    limpiador()
    print("Nombre de los estudiantes:\n", estudiantes_nombres)
    print()
    print("Apellido de los estudiantes: \n", estudiantes_apellidos)
    print()
    print("Carnet de identidad de los estudiantes: \n", estudiantes_CI)
    print()
    print("Año de nacimiento de los estudiantes: \n", estudiantes_fecha)
    print()
    print("Telefono de los estudiantes: \n", estudiantes_telefono)
    print()


def adicionar_estudiantes():
    # limpiador de pantalla
    limpiador()
    # nombres
    estudiantes_nombres.append(input("Ingrese los nombres del estudiante: "))
    # apellidos
    estudiantes_apellidos.append(input('Ingrese los apellidos del estudiante: '))
    # CI
    estudiantes_CI.append(input('Ingrese el CI del estudiante: '))
    # Fecha de nacimiento
    estudiantes_fecha.append(int(input('Ingrese la fecha de nacimiento del estudiante: ')))
    # Telefono
    estudiantes_telefono.append(input('Ingrese el telefono del estudiante: '))
    print("\033[4;30;47m", 'Se han guardado los datos del nuevo estudiante', '\033[0;m')
    print()


def modificar_estudiante():
    limpiador()
    carnet_modificar = input("Introduzca el CI del estudiante a modificar: ")
    while True:
        if carnet_modificar in estudiantes_CI:
            posicion = estudiantes_CI.index(carnet_modificar)
            estudiantes_nombres[posicion] = input("Ingrese el nuevo Nombre: ")
            estudiantes_apellidos[posicion] = input("Ingrese el nuevo Apellido: ")
            estudiantes_CI[posicion] = input("Ingrese el nuevo CI: ")
            estudiantes_fecha[posicion] = int(input("Ingrese el nuevo año de nacimiento: "))
            estudiantes_telefono[posicion] = input("Ingrese el nuevo telefono: ")
            break
        else:
            carnet_modificar = input("El carnet que ingreso no existe. Intente otra vez: ")


def eliminar_estudiante():
    limpiador()
    # ciBorrar = input('Ingrese el Carnet de Identidad del estudiante a borrar: ')
    # posicion = estudiantes_CI.index(ciBorrar)
    carnet_modificar = input("Introduzca el CI del estudiante a modificar:\n")
    print()
    while True:
        if carnet_modificar in estudiantes_CI:
            posicion = estudiantes_CI.index(carnet_modificar)
            print("\033[4;30;47m", 'El estudiante', estudiantes_nombres[posicion], estudiantes_apellidos[posicion],
                  'se elimino correctamente. ',  '\033[0;m')
            print()
            print()
            estudiantes_nombres.pop(posicion)
            estudiantes_apellidos.pop(posicion)
            estudiantes_CI.pop(posicion)
            estudiantes_fecha.pop(posicion)
            estudiantes_telefono.pop(posicion)
            break
        else:
            carnet_modificar = input("El carnet que ingreso no existe. Intente otra vez: ")
            print()


# Ingresar un dia y mostrar a los estudiantes que pueden salir ese dia
def consultar_salida():
    # limpiador
    limpiador()
    # Lun Mie Vie   impares
    # Mar Jue Sab   pares
    dia = input('Ingrese el dia que se desea validar (lun mie vie mar jue sab): ').lower()
    comparador = -1
    # LUN lun Lun LuN
    if dia in ['lun', 'mie', 'vie']:
        comparador = 1
        print('Los estudiantes que pueden salir son:\n')
    elif dia in ['mar', 'jue', 'sab']:
        comparador = 0
        print('Los estudiantes que pueden salir son:\n')
    else:
        print('Dia no registrado')
    for i in range(len(estudiantes_nombres)):
        if int(estudiantes_CI[i]) % 2 == comparador:
            print("\033[4;30;47m", estudiantes_nombres[i], " ", estudiantes_apellidos[i], '\033[0;m')
            print("\033[4;30;47m", estudiantes_CI[i], '\033[0;m')
            print()


def consultar_edad():
    limpiador()
    ano_actual = datetime.now()
    carnet_modificar = input("Introduzca el CI del estudiante a calcular:\n")
    print()
    while True:
        if carnet_modificar in estudiantes_CI:
            estudiante_indice = int(estudiantes_CI.index(carnet_modificar))
            print("La edad de", "\033[4;30;47m", estudiantes_nombres[estudiante_indice], '\033[0;m', " es ",
                  "\033[4;30;47m", 2020 - estudiantes_fecha[estudiante_indice], '\033[0;m')
            print()
            break
        else:
            limpiador()
            carnet_modificar = input("El carnet que ingreso no existe. Intente otra vez: ")


def limpiador():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


switch = True
while switch:
    limpiador()
    mostrar_menu()
    opcion = input()
    if opcion == '1':
        print('Esta es la lista de estudiantes registrados')
        mostrar_estudiantes()
    elif opcion == '2':
        print('Ingrese los datos del estudiante nuevo')
        adicionar_estudiantes()
    elif opcion == '3':
        modificar_estudiante()
    elif opcion == '4':
        eliminar_estudiante()
    elif opcion == '5':
        consultar_salida()
    elif opcion == '6':
        consultar_edad()
    elif opcion == '0':
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opcion no valida.")
        break
    respuesta_usuario = input(
        "La tarea se ejecuto correctamente, desea realizar alguna otra operacion? (S/N)\n").lower()
    while True:
        if respuesta_usuario == 's':
            switch = True
            limpiador()
            break
        elif respuesta_usuario == 'n':
            switch = False

            print("\033[4;30;47m", 'Gracias por utilizar el sistema.', '\033[0;m')
            break
        else:
            respuesta_usuario = input("Ingrese una opción valida:\n")

# TODO: PERSISTENCIA

