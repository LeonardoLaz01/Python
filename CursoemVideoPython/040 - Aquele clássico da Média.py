nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'suas notam foram {nota1} e {nota2} e sua média é {media}.')
if media < 5.0:
    print('REPROVADO')
elif media <= 5.0 or media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
