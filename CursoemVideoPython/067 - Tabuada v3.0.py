valor = int(input('Quer ver a tabuada de qual valor? '))
while True:
    print('-' * 20)
    for c in range(1, 11):  # Tabuada
        print(f'{valor} x {c} = {valor * c}')  # Valor inserido x contador do for
    print('-' * 20)
    valor = int(input('Quer ver a tabuada de qual valor? '))  # Checando se o usuário quer continuar
    if valor < 0:  # Se o número é negativo o programa para
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
