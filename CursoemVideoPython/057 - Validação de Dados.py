nome = str(input('Digite seu nome: ')).strip().title()  # Nome
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()  # Sexo
while sexo not in 'MF':   # Repetir enquanto váriavel 'sexo' não for masculino ou feminino
    sexo = str(input('Opção inválida. Tente novamente: ')).strip().upper()
if sexo == 'M':  # Escrevendo por extenso
    genero = 'Masculino'
else:
    genero = 'Feminino'
print(f'Olá {nome}, você é do sexo {genero}')  # Mostrando ao usuário
