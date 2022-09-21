def ficha(nome = '', gols = 0):
    if not nome:
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato')


nome = (input('Nome do jogador: '))
gols = (input('Número de Gols: '))
ficha(nome, gols)  