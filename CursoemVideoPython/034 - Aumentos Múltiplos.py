salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento = (15 / 100) * salario
else:
    aumento = (10 / 100) * salario
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario+aumento:.2f} agora')
