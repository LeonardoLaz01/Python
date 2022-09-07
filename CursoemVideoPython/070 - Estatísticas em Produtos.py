total = caro = baratopreco = cont = 0
baratonome = ''
while True:
    cont += 1
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < baratopreco:
        baratonome = produto
        baratopreco = preco
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('-' * 40)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baratonome} que custa R${baratopreco:.2f}')
