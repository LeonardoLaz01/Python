jogador = dict()
lista = list()
while True:
    print('-' * 50)
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols = list()
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {p + 1}ª partida? ')))
        jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    lista.append(jogador.copy())
    print('-' * 50)
    while True:
        continuar = str(input('Deseja continuar? ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar in 'Nn':
        break
print('-=' * 50)
print(f'{"Cod":<10}{"Nome":<10}{"Gols":<25}{"Total":<25}')
print('-' * 50)
for j in enumerate(lista):
    print(f'{j[0]:<10}{j[1]["Nome"]:<10}{(str(j[1]["Gols"])):<25}{j[1]["Total"]:<25}')
print('-' * 50)
while True:
    cont = 1
    levantamento = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if levantamento == 999:
        break
    elif levantamento < len(lista):
        print(f'--Levantamento do jogador {lista[levantamento]["Nome"]}')
        for j in enumerate(lista):
                for g in j[1]["Gols"]:
                    print(f'   No jogo {cont} fez {g} gols.')
                    cont += 1
    else:
        print(f'ERRO! não existe jogador com código {levantamento}!')
        continue
    print('-' * 50)
print('<< ENCERRADO >>')   
