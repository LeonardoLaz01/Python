num = total = soma = 0
while num != 999:
    if num < 999:
        num = int(input('Digite um número [999 para parar]: '))
        total = total + 1
        soma += num
print(f'Você digitou {total-1} números e a soma deles foi {soma-999}')
