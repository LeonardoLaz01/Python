from time import sleep
from random import randint
from operator import itemgetter
valores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for jogador, dado in valores.items():
    print(f'{jogador} tirou {dado} no dado.')
    sleep(1)
print('-=' * 30)
print('== RANKING DOS JOGAODRES ==')
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
for key, value in enumerate(ranking):
    print(f'{key + 1} lugar: {value[0]} com {value[1]}.')
