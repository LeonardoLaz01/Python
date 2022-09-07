frase = str(input('Frase: ')).strip().upper().replace(' ', '')
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
