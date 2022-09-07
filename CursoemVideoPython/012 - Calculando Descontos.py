preco = float(input('Qual é o preço do produto? R$'))
desconto = (5 / 100) * preco
print(f'O produto que custava R${preco:.2f} na promoção com desconto de 5% vai custar R${preco - desconto:.2f}')
