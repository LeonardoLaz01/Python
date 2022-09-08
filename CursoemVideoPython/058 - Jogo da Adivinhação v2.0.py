from random import randint
pc = randint(1, 10)
cont = 0
jogador = int(input('Escolha um número entre 1 e 10: '))
while jogador != pc:
    jogador = int(input(f'Você errou, o computador pensou no número {pc}. Tente novamente: '))
    cont += 1
    pc = randint(1, 10)
if jogador == pc:
    print(f'Você ganhou! o computador pensou no número {pc}. Você precisou de {cont} tentativa(s).')
