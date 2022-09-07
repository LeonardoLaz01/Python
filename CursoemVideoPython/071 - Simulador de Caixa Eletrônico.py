print('Banco do Leozinho')
saque = int(input('que valor você quer sacar? R$'))
ced = 0
while True:
    if saque != 0:
        ced = saque // 50
        if ced != 0:
            print(f'Total de {ced} cédulas de R$50')
        saque = saque % 50
    if saque != 0:
        ced = saque // 20
        if ced != 0:
            print(f'Total de {ced} cédulas de R$20')
        saque = saque % 20
    if saque != 0:
        ced = saque // 10
        if ced != 0:
            print(f'Total de {ced} cédulas de R$10')
        saque = saque % 10
    if saque != 0:
        ced = saque // 1
        if ced != 0:
            print(f'Total de {ced} cédulas de R$1')
        saque = saque % 1
    else:
        break
print('Volte sempre ao Banco do Leozinho. Tenha um bom dia!')
