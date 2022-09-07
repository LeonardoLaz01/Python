casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Em quantos anos você irá pagar? '))
prestacao = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
porcentagem = (30 / 100) * salario
if prestacao > porcentagem:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
