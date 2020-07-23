import random
regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv','patı́n','balón', 'reloj', 'bicicleta', 'anillos']
for serie in range(2):
    print('\n serie:', serie + 1)
    random.seed(0)
    for sorteo in range(5):
        regalo = regalos[random.randint(0, 9)]
        print('Sorteo', sorteo + 1, ':', regalo)