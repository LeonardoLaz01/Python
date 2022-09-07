media = 0
maior = 0
velho = ''
muie = 0
for c in range(1, 5):
    print(f'--------{c}ª PESSOA--------')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            velho = nome
    if sexo == 'F' and idade < 20:
        muie += 1
print(f'A média de idade do grupo é de {media / 4} anos')
print(f'O homem mais velho tem {maior} anos e se chama {velho}')
print(f'Ao todo são {muie} mulheres com menos de 20 anos')
