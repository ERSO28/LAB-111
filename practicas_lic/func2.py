#Rivera Valencia Juan Alejandro 6924042lp

def ocurrencias(primer_numero, segundo_numero):
    contador = 0
    while primer_numero >= segundo_numero:
        if primer_numero >= segundo_numero:
            contador += 1
            primer_numero = primer_numero - segundo_numero
    return contador


primer_numero = int(input("Introduzca el primer numero: "))
segundo_numero = int(input("Introduzca el segundo:  "))

print("La cantida de ocurrencias son: ",ocurrencias(primer_numero, segundo_numero))