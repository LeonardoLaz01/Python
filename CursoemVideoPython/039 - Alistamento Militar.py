from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade < 18:
    print(f'Você tem {idade} em {ano} e ainda vai se alistar. Faltam {18 - idade} anos.')
    print(f'Seu alistamento será em {nascimento + 18}.')
elif idade == 18:
    print(f'Você tem {idade} em {ano} e já pode se alistar.')
else:
    print(f'Você tem {idade} em {ano} seu prazo de alistamento está atrasado em {idade - 18} anos.')
    print(f'Você deveria ter se alistado em {18 + nascimento}.')
