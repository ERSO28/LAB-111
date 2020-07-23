#Rivera Valencia Juan Alejandro 6924042lpe.
import random

for i in range(3):
    numero1 = int(random.randrange(65, 90))
    numero2 = int(random.randrange(65, 90))
    numero3 = int(random.randrange(65, 90))

if numero3 < numero1 and numero2 < numero1:
    if numero3 < numero2:
        print(numero3, numero2, numero1)
    else:
        print(numero2, numero3, numero1)
else:
    if numero2 < numero3:
        if numero1 < numero2:
            print(numero1, numero2, numero3)
        else:
            print(numero2, numero1, numero3)
    else:
        if numero1 < numero3:
            print(numero1, numero3, numero2)
        else:
            print(numero3, numero1, numero2)