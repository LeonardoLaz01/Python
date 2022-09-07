aluno = []
cont = 0
while True:
    aluno.append([])
    aluno[cont].append(str(input('Nome: ')))
    aluno[cont].append(float(input('Nota 1: ')))
    aluno[cont].append(float(input('Nota 2: ')))
    media = float(f'{(aluno[cont][1] + aluno[cont][2]) / 2:.1f}')
    aluno[cont].append(media)
    cont += 1
    continuar = input('Quer continuar? ')
    if continuar in 'Nn':
        break
print(f'{"Nº":^10}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 50)
for a in range(0, len(aluno)):
    print(f'{a:^10}{aluno[a][0]:<10}{aluno[a][3]:>10}')
print('-' * 50)
while True:
    op = int(input('Mostrar notas de qual aluno? (999 imterrompe): '))
    if op == 999:
        print('Encerrando programa...')
        break
    else:
        print(f'Notas de {aluno[op][0]} são {aluno[op][1:3]}')
        print('-' * 50)
