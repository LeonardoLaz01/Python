lista = []
for i in range(0, 5):
    x = int(input('Digite um valor: '))
    if i == 0 or x > lista[-1]:
        lista.append(x)
    else:
        y = 0
        while y < len(lista):
            if x <= lista[y]:
                lista.insert(y, x)
                break
            y += 1
print(f'Lista em Ordem: {lista}')
