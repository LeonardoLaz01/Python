import modulos
preco = float(input('Digite o preco: R$'))
print(f'A metade de {modulos.moeda(preco)} é {modulos.moeda(modulos.metade(preco))}')
print(f'O dobro de {modulos.moeda(preco)} é {modulos.moeda(modulos.dobro(preco))}')
print(f'Aumentando 10%, temos {modulos.moeda(modulos.aumento(preco, 10))}')
