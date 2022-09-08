lista = list()
dicionario = dict()
soma = 0
while True:
    dicionario['Nome'] = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF':
        print('ERRO! Por favor, digite aoenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    dicionario['Sexo'] = sexo
    dicionario['Idade'] = int(input('Idade: '))
    soma += dicionario['Idade']
    lista.append(dicionario.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Ss':
        continue
    elif continuar in 'Nn':
        break
    else:
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
print('-=' * 30)
media = soma / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print('\nD) Lista das pessoas com idade acima da média:')
for pessoa in lista:
    if pessoa['Idade'] > media:
        print(f'    Nome = {pessoa["Nome"]}; sexo = {pessoa["Sexo"]}; idade = {pessoa["Idade"]};')
print('<< ENCERRADO >>')
