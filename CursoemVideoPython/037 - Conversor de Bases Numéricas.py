num = int(input('Escreva um número inteiro: '))
base = int(input('1 para binário \n2 para octal \n3 para hexadecimal \nEscolha um número para conversão: '))
if base == 1 or 2 or 3:
    if base == 1:
        print(bin(num)[2:])
    elif base == 2:
        print(oct(num)[2:])
    elif base == 3:
        print(hex(num)[2:])
else:
    print('Escolha um número válido e tente novamente.')
