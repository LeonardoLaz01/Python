jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols = list()
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {p + 1}ª partida? ')))
    jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for p in enumerate(jogador['Gols']):
    print(f'Na {p[0] + 1}ª partida, fez {p[1]} gols')
print(f'Foi um total de {jogador["Total"]} gols')
