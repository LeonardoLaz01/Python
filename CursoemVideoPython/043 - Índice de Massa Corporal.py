peso = float(input('Peso: '))
altura = float(input('Altura: '))
IMC = peso / pow(altura, exp = 2)
print(f'O IMC dessa pessoa é de {IMC:.1f}')
if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC <= 25:
    print('Peso ideal')
elif IMC <= 30:
    print('sobrepeso')
elif IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
