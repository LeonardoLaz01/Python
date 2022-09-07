from random import choice
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
escolha = choice([primeiro, segundo, terceiro, quarto])
print(f'O aluno escolhido foi {escolha}')
