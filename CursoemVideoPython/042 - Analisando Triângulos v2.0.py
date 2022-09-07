# condições para formar um triãngulo e o seu tipo
lado1 = int(input('Primeiro lado: '))
lado2 = int(input('Segundo lado: '))
lado3 = int(input('terceiro lado: '))  # Leitura dos segmentos
if lado1 != 0 and lado2 != 0 and lado3 != 0:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:  # Validação dos segmentos
        if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
            print('Triângulo Equilátero')
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print('Triângulo Escaleno')
        else:
            print('Triângulo Isósceles')  # Indentificação do tipo de triângulo
    else:
        print('Um dos lados não pode formar um triângulo')
else:
    print('Um dos lados não pode formar um triângulo')  # Invalidação caso os segmentos não formem um triângulo
