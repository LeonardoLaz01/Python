pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['Idade'] = 2022 - ano
pessoa['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['Ctps']:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] - ano) + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k}: {v}')
