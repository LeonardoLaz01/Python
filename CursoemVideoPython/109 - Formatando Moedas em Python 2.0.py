import modulos
preco = float(input('Digite o preço: R$'))
print(f'A metade de {modulos.moeda(preco)} é {modulos.metade(preco, True)}')
print(f'O dobro de {modulos.moeda(preco)} é {modulos.dobro(preco, True)}')
print(f'Aumentado 10%, temos {modulos.aumento(preco, 10, True)}')
print(f'Reduzindo 13%, temos {modulos.diminuir(preco, 13, True)}')
