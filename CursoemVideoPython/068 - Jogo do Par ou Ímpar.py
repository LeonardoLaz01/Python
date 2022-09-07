from random import randint
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
valor = int(input('Diga um valor: '))
escolha = str(input('Par ou ímpar [P/I] ')).strip().upper()
pc = randint(1, 10)
cont = 0
while True:
    res = valor + pc
    print('-' * 50)
    print(f'você jogou {valor} e o computador {pc}. total de {res}')
    print('-' * 50)
    if escolha == 'P':
        if res % 2 == 0:
            print('Venceu')
            print('vamos jogar novamente...')
            print('-=' * 20)
            valor = int(input('Diga um valor: '))
            escolha = str(input('Par ou ímpar [P/I] ')).strip().upper()
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        if escolha == 'I':
            if res % 2 == 1:
                print('Você VENCEU!')
                print('Vamos jogar novamente...')
                print('-=' * 20)
                valor = int(input('Diga um valor: '))
                escolha = str(input('Par ou ímpar [P/I] ')).strip().upper()
                cont += 1
            else:
                print('Você PERDEU!')
                break
print('-=' * 20)
print(f'GAME OVER! Você venceu {cont} vezes')
