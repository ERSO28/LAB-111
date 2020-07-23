#Rivera Valencia Juan Alejandro     6924042lp

a = int(input("Ingrese un numero:   "))
lista = []
contador = 1

while a != 0:
    lista.insert(contador, a)
    a = int(input("Ingrese un numero:   "))
    lista.sort(reverse=True)

print(lista)