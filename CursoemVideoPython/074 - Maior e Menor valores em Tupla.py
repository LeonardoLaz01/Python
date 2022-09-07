from random import randint
cu = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = 0
menor = 0
for i in range(0, len(cu)):
    if i == 0:
        maior = cu[i]
        menor = cu[i]
    if cu[i] > maior:
        maior = cu[i]
    if cu[i] < menor:
        menor = cu[i]

print(f'Os valores sorteados foram: {cu}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
