maior = 0
menor = 9999999999999999
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi {maior}Kg')
print(f'O menor peso foi {menor}Kg')
