from random import sample
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
print('A ordem de apresetanção será:')
print(sample(lista, k=4))
