from random import randint
def sorteando(lista):
    print('Sorteando 5 valores da lista:', end= ' ')
    for i in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        lista.append(n)
    print('PRONTO!')


def soma(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


lista = list()
sorteando(lista)
soma(lista)