tupla = (int(input('Digite um número: ')), int(input('digite outro número: ')), int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print('Você digitou os valores', tupla)
print(f'O valor 9 apareceu {tupla.count(9)}ª vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
