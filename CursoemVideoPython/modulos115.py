def interface(msg):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


def verpessoas():
    try:
        arquivo = open('cadastro.txt', 'r')
    except:
        arquivo = open('cadastro.txt', 'wt+')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastropessoas():
    arquivo = open('cadastro.txt', 'a')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    arquivo.write(f'{nome};{idade}\n')


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
                interface('PESSOAS CADASTRADAS')
                verpessoas()
            elif op == 2:
                interface('NOVO CADASTRO')
                cadastropessoas()
            elif op == 3:
                interface(f'Saindo do sistema...até logo!')
                break
            else:
                print('ERRO: Digite uma opção válida!')
                continue
