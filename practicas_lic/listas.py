#Rivera Valencia Juan Alejandro     6924042lp

cadena = input("Introduzca una palabra\n")
cadena_sin_espacios = cadena.replace(" ","")
cadena_invertida = ""

for letra in cadena_sin_espacios:
    cadena_invertida = letra + cadena_invertida

if cadena_sin_espacios == cadena_invertida:
    print("Palindrome")
else:
    print("No palindrome")

