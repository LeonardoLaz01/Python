largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
m2 = largura*altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {m2}m²')
print(f'Para pintar essa parede, você precisará de {m2/2}l de tinta.')
