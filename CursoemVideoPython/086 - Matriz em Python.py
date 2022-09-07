matriz = [[], [], []]
cont = 0
for i in range(0, 3):
    for lista in matriz:
        x = int(input(f'Digite um valor para: {[i, cont]}: '))
        cont += 1
        if cont == 3:
            cont = 0
        matriz[i].append(x)
for lista in matriz[0]:
    print(f'[{lista:^5}]', end=' ')
print()
for lista in matriz[1]:
    print(f'[{lista:^5}]', end=' ')
print()
for lista in matriz[2]:
    print(f'[{lista:^5}]', end=' ')
