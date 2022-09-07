valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('''Escolha uma das opções: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
op = int(input('Opção: '))
while op != 5:
    if op == 1:
        print(f'A soma entre {valor1} e {valor2} é igual à {valor1+valor2}')
        op = int(input('Deseja fazer outra operação? '))
    elif op == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é igual à {valor1+valor2}')
        op = int(input('Deseja fazer outra operação? '))
    elif op == 3:
        if valor1 > valor2:
            print('O primeiro valor é maior')
        else:
            print('O segundo valor é maior')
        op = int(input('deseja fazer outra operação? '))
    elif op == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite outro novo valor: '))
        op = int(input('Deseja fazer outra operação? '))
    elif op == 5:
        print('Fim do programa.')
    else:
        op = int(input('Operador Inválido. tente novamente: '))
