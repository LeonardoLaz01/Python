from datetime import date
nascimento = int(input('Ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
