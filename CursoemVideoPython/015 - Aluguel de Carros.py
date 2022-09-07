dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
calc = (60 * dias) + (0.15*km)
print(f'O total a pagar é de R${calc:.2f}')
