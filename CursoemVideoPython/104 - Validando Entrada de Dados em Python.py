def leiaint(inputnum):
    n = input(inputnum)
    while not n.isnumeric():
        print('ERRO! digite um número inteiro válido.')
        n = input('Digite um número: ')
    else:
        return n
        

n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')
