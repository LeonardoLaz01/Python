# 10 termo de uma PA
termo = int(input('Primeiro termo: ')) # Primeiro termo
razao = int(input('Razão: '))  # Razão
decimo = termo + (10 - 1) * razao  # os 10 primeiros termos de uma PA
for c in range(termo, decimo+razao, razao):
    print(c, end=' > ')
print('Acabou')
