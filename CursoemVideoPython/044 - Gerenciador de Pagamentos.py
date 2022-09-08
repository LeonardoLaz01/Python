produto = float(input('valor do produto: R$'))
print('''Escolha uma das opções de pagamento:
[ 1 ] À vista no dinheiro/cheque com 10% de desconto
[ 2 ] À vista no cartão com 5% de desconto
[ 3 ] Em até 2x no cartão sem juros
[ 4 ] Em 3x ou mais no cartão com 20% de juros''')
pagamento = int(input('Opção: '))
if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    if pagamento == 1:
        desconto = produto - (10 / 100) * produto
        print(f'O produto que custava R${produto:.2f} passa a custar R${desconto:.2f} com pagamento à vista no'
              f'dinheiro ou cheque')
    elif pagamento == 2:
        desconto = produto - (5 / 100) * produto
        print(f'O produto que custava R${produto:.2f} passa a custar R${desconto:.2f} com pagamento à vista no cartão')
    elif pagamento == 3:
        print(f'O produto será parcelado em 2x no cartão sem juros, o valor da parcela será R${produto / 2:.2f}'
              f'e o valor final será R${produto:.2f}.')
    else:
        vezes = int(input('Em quantas vezes o valor será parcelado? (O produto deve ser parcelado no'
                          'mínimo até 3x) '))
        if vezes >= 3:
            parcelas = produto / vezes
            juros = parcelas + (20 / 100) * parcelas
            print(f'O produto será parcelado em {vezes}x no cartão com 20% de juros, o valor da parcela será'
                  f' R${juros:.2f} e o valor final será R${produto + (20 / 100) * produto:.2f}')
        else:
            print('Opção inválida. Tente novamente')
else:
    print('Opção inválida. Tente novamente.')