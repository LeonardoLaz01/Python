from datetime import date
anoatual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input(f'ano de nascimento da {c}ª pessoa: '))
    if anoatual - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print(f'{menores} pessoas ainda não atingiram a maior idade')
print(f'{maiores} pessoas já são maiores de idade')
