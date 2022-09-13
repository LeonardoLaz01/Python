def calculo(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')


largura = float(input('LARGURA (m) '))
comprimento = float(input('COMPRIMENTO (m) '))
print('Controle de Terrenos')
print('-' * 50)
calculo(largura, comprimento)
