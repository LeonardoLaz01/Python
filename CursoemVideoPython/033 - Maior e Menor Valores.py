primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('terceiro valor: '))
maior = primeiro
menor = primeiro
if segundo > maior and segundo > terceiro:  # Verificando o maior
    maior = segundo
if terceiro > maior and terceiro > segundo:
    maior = terceiro
print(f'O maior valor digitado foi {maior}')
if segundo < menor and segundo < terceiro:  # Verificando o menor
    menor = segundo
if terceiro < menor and terceiro < segundo:
    menor = terceiro
print(f'O menor valor digitado foi {menor}')
