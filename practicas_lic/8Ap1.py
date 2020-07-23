#Juan Alejandro Rivera Valencia     6924042lp

cadena = input("Introduce un cadena:\n")
cadena_sin_espacios = cadena.replace(" ","")
lista = []
for i in cadena_sin_espacios:
    lista.append(i)
print(lista)

