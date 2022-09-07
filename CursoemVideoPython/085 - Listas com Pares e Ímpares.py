lista = [[], []]
for i in range(1, 8):
    x = int(input(f'Digite o {i}º valor: '))
    if x % 2 == 0:
        lista[0].append(x)
    if x % 2 == 1:
        lista[1].append(x)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
