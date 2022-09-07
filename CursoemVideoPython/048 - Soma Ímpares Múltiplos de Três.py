soma = 0
valor = 0
for contador in range(1, 501):  # Contagem de 1 até 500
    if contador % 2 == 1:  # Verificando se o número é ímpar
        if contador % 3 == 0:  # Verificando se o número é múltiplo de 3
            soma = soma + contador  # Váriavel soma recebe a soma de todos os valores
            valor = valor + 1  # Váriavel valor recebe a quantidade de números ímpares divisiveis por três
print(f'A soma de todos os {valor} valores solicitados é {soma}')
