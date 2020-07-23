#Juan Alejandro Rivera Valencia     6924042lp

cadena = input("Introduza su cadena:\n")
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(lista)