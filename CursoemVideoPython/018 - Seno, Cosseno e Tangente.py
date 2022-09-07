import math
angulo = int(input('Digite o ângulo que você deseja: '))
convert = math.radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {math.sin(convert):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {math.cos(convert):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {math.tan(convert):.2f}')
