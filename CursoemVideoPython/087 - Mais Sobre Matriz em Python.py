matriz = [[], [], []]
cont = soma = 0
for i in range(0, 3):
    for lista in matriz:
        x = int(input(f'Digite um valor para: {[i, cont]}: '))
        if x % 2 == 0:
            soma += x
        cont += 1
        if cont == 3:
            cont = 0
        matriz[i].append(x)
print('-=' * 30)
for lista in matriz[0]:
    print(f'[{lista:^5}]', end=' ')
print()
for lista in matriz[1]:
    print(f'[{lista:^5}]', end=' ')
print()
for lista in matriz[2]:
    print(f'[{lista:^5}]', end=' ')
print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
