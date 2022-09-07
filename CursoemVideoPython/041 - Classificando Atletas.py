# A Confederação Nacional precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade
from datetime import date
nascimento = int(input('Ano de nascimento do atleta: '))
anoatual = date.today().year # Ano atual
idade = anoatual - nascimento # Idade do atleta
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
