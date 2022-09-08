soma = 0
valor = 0
for contador in range(1, 501):
    if contador % 2 == 1:
        if contador % 3 == 0:
            soma = soma + contador
            valor = valor + 1
print(f'A soma de todos os {valor} valores solicitados é {soma}')
