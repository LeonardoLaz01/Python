from random import randint
pc = randint(1, 10)  # Jogada do computador
cont = 0  # Número de tentativas do jogador
jogador = int(input('Escolha um número entre 1 e 10: '))  # Número do jogador
while jogador != pc:  # Repetir enquanto o jogador não adivinhar o número do computador
    jogador = int(input(f'Você errou, o computador pensou no número {pc}. Tente novamente: '))
    cont += 1
    pc = randint(1, 10)
if jogador == pc:  # Se Acertar, o programa se encerra
    print(f'Você ganhou! o computador pensou no número {pc}. Você precisou de {cont} tentativa(s).')
