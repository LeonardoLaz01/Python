def maior(*n):
    print('-=' * 30)
    m = cont = 0
    if n:
        m = max(n)
        cont = len(n)
    print('Analisando os valores passados...')
    for i in n:
        print(i, end=' ')
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
