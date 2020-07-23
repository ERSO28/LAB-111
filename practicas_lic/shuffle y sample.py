import random
transporte = ['bici', 'moto', 'coche', 'tren', 'avión']
print('Hoy viajaré en: ', random.choice(transporte), "\n")


lista1 = ['rojo', 'verde', 'amarillo']
random.shuffle(lista1)
print('mezcla1', lista1)
print(lista1[random.randint(0,2)], "\n")


lista2 = ['x', 'y', 'z']
print(random.sample(lista2, 2))