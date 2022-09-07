lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
