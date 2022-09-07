total = soma = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    total += 1
    soma += valor
print(f'A soma dos {total} valores foi {soma}!')
