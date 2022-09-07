cadastros = list()
dado = list()
maiores = list()
menores = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    cadastros.append(dado[:])
    dado.clear()
    continuar = input('Deseja continuar? ')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'O total de pessoas cadastradas são {len(cadastros)}.')
for i in range(0, len(cadastros)):
    if i == 0:
        maior = cadastros[i][1]
    else:
        if cadastros[i][1] > maior:
            maior = cadastros[i][1]

for pessoa in cadastros:
    if pessoa[1] == maior:
        maiores.append(pessoa[0])

print(f'O maior peso foi {maior}Kg. Peso de {maiores}.')

for i in range(0, len(cadastros)):
    if i == 0:
        menor = cadastros[i][1]
    else:
        if cadastros[i][1] < menor:
            menor = cadastros[i][1]

for pessoa in cadastros:
    if pessoa[1] == menor:
        menores.append(pessoa[0])
print(f'O menor peso foi {menor}Kg. Peso de {menores}.')
