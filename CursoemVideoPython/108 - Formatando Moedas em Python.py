from utilidadesCeV.moeda import moeda, metade, dobro, aumento
preco = float(input('Digite o preco: R$'))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(aumento(preco, 10))}')
