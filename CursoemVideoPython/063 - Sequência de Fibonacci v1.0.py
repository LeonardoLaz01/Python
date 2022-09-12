print('-' * 50)
print('Sequência de Fibonacci')
print('-' * 50)
termos = int(input('Quantos termos você quer mostrar? '))
print('~' * 50)
x = cont = 0
y = 1
while cont < termos:
    print(x, end=' -> ')
    cont += 1
    z = x + y
    x = y
    y = z
print('FIM', end='')
print()
print('~' * 50)
