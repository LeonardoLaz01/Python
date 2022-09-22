def PyHelp():
    from time import sleep
    while True:
        print('~' * 30)
        print('   SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        foub = str(input('Função ou Biblioteca > ')).lower()
        if foub == 'fim':
            print('~' * 20)
            print('     ATÉ LOGO!')
            print('~' * 20)
            break
        print('~' * 50)
        print(f'      Acessando o manual do comando {foub}')
        print('~' * 50)
        sleep(1.5)
        help(foub)


PyHelp()
