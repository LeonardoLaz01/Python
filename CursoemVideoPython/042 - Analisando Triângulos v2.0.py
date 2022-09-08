lado1 = int(input('Primeiro lado: '))
lado2 = int(input('Segundo lado: '))
lado3 = int(input('terceiro lado: '))
if lado1 != 0 and lado2 != 0 and lado3 != 0:
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
            print('Triângulo Equilátero')
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print('Triângulo Escaleno')
        else:
            print('Triângulo Isósceles')
    else:
        print('Um dos lados não pode formar um triângulo')
else:
    print('Um dos lados não pode formar um triângulo')
