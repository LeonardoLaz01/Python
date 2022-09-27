from utilidadesCeV.moeda import metade, dobro, aumento
preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${metade(preco)}')
print(f'O dobro de R${preco} é R${dobro(preco)}')
print(f'Aumentando 10%, temos R${aumento(preco, 10)}')
