maior = homens = mulheres = 0
while True:
    print('-' * 50)
    print('CADASTRE UMA PESSOA')
    print('-' * 50)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        homens += 1
    else:
        if sexo == 'F' and idade < 20:
            mulheres += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('========FIM DO PROGRAMA=========')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
