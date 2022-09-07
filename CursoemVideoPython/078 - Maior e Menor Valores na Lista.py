lista = []
for x in range(0, 5):
    y = int(input(f'Digite um valor para a posição {x}: '))
    lista.append(y)
print(f'Você digitou os valores {lista}')
maior = max(lista)
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for n in range(0, len(lista)):
    if maior == lista[n]:
        print(f'{n:.<4}', end=' ')
menor = min(lista)
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for n in range(0, len(lista)):
    if menor == lista[n]:
        print(f'{n:.<4}', end=' ')
