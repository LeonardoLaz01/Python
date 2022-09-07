from random import choice
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
numero = choice([0, 1, 2, 3, 4, 5])
jogador = int(input('Em que número eu pensei? '))
if numero == jogador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero} e não no {jogador}')
