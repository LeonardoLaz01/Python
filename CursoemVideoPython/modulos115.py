def interface(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


def menu():
    while True:
        interface('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair do sistema')
        print('-' * 40)
        try:
            op = int(input('Sua opção: '))
        except ValueError:
            print('ERRO: por favor, digite um número inteiro válido')
        else:
            if op == 1:
                interface(f'Opção {op}')
            elif op == 2:
                interface(f'Opção {op}')
            elif op == 3:
                interface(f'Saindo do sistema...até logo!')
                break
            else:
                print('ERRO: Digite uma opção válida!')
                continue
