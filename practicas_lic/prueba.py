import random
numero = int(input("Escribe tu numero >> "))
cpu = random.choice(range(10))
valor = cpu + numero
print ("\nNúmero elegido por la computadora:",cpu)
print ("La suma de los números es" , valor)
if (valor % 2 == 0):
    print ("\nEs par  Has ganado")
else:
    print ("\nEs impar Perdiste, gana la computadora")