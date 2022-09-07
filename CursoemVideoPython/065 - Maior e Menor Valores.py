continuar = 'S'
cont = soma = num = maior = menor = 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} números e a média foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
