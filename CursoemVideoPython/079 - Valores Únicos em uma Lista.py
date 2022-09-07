lista = []
while True:
    x = int(input('Digite um valor: '))
    if x not in lista:
        lista.append(x)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
print(20 * '-=')
print('Você digitou os valores', sorted(lista))
