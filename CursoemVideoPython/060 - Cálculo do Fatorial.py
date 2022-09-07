from math import factorial
x = int(input('Digite um número para calcular seu Fatorial: '))
y = 0
soma = 0
while y != x:
    y += 1
    print((x - y) + 1, end=' > ')
print(factorial(x))
