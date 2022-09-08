nome = str(input('Digite seu nome: ')).strip().title()
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Opção inválida. Tente novamente: ')).strip().upper()
if sexo == 'M':
    genero = 'Masculino'
else:
    genero = 'Feminino'
print(f'Olá {nome}, você é do sexo {genero}')
