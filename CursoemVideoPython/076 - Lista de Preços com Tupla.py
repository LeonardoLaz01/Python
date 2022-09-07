tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 50)
print(f'{"Listagem de Preços":^50}')
print('-' * 50)
for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<40}', f'R${tupla[i+1]:>7.2f}')
print('-' * 50)
