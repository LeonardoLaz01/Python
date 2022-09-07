from time import sleep
from random import randint
lista = []
print('-' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-' * 30)
x = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {x} JOGOS -=-=-=')
for i in range(0, x):
    lista.append([])
    for n in range(0, 6):
        y = randint(1, 60)
        if y not in lista[i]:
            lista[i].append(y)
    print(f'Jogo {i+1}: {sorted(lista[i])}')
    sleep(1)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')
