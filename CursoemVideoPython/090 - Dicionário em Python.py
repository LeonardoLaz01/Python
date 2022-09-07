aluno = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if aluno['Média'] > 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 30)
print('Nome:', aluno['Nome'])
print('Média:', aluno['Média'])
print('A Situação do aluno é:', aluno['Situação'])
