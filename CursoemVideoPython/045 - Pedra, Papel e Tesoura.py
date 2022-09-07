from random import randint
from time import sleep
# Jokenpo
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))  # Jogada do usuário
pc = randint(0, 2)  # Jogada do computador
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if jogador == 0 or jogador == 1 or jogador == 2: # Validando escolha
    print('=-' * 15)
    if pc == 0:
        print('computador jogou Pedra')
    elif pc == 1:
        print('Computador jogou Papel')
    else:
        print('computador jogou Tesoura')
    if jogador == 0:
        print('Jogador jogou Pedra')
    elif jogador == 1:
        print('Jogador jogou Papel')
    else:
        print('Jogador jogou Tesoura')
    print('-=' * 15)
else:
    print('Opção inválida. tente novamente')
if jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1: # Resultado
    print('JOGADOR VENCEU')
elif pc == 0 and jogador == 2 or pc == 1 and jogador == 0 or pc == 2 and jogador == 1:
    print('COMPUTADOR VENCEU')
else:
    print('EMPATE')
