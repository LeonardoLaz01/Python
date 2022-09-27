from utilidadesCeV.moeda import moeda, dobro, metade, aumento, diminuir

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preco)} é {metade(preco, True)}')
print(f'O dobro de {moeda(preco)} é {dobro(preco, True)}')
print(f'Aumentado 10%, temos {aumento(preco, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(preco, 13, True)}')
