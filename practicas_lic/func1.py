#Rivera Valencia Juan Alejandro 6924042lp

def descom(numero_de_usuario):
    sumDigit, extNum = 0, 0
    while numero_de_usuario != 0:
        extNum = numero_de_usuario % 10
        numero_de_usuario //= 10
        sumDigit += extNum
    return sumDigit


numero_de_usuario = int(input("Introduzca un numero:   "))
while numero_de_usuario != 0:
    resultado = descom(numero_de_usuario)
    print("La suma de sus digitos son: ",resultado)
    numero_de_usuario = int(input("Introduzca otro numero:   "))
print("Ingreso 0")
