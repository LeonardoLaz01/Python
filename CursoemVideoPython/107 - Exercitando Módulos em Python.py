import modulos
preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${modulos.metade(preco)}')
print(f'O dobro de R${preco} é R${modulos.dobro(preco)}')
print(f'Aumentando 10%, temos R${modulos.aumento(preco, 10)}')
