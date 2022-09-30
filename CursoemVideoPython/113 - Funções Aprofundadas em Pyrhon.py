def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except ValueError:
            print('ERRO: Por favor, digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except ValueError:
            print('ERRO: Por favor, digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
