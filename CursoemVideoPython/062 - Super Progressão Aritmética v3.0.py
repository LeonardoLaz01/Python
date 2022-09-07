primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
escolha = 10
total = 0
while escolha != 0:
    total += escolha
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    escolha = int(input("Quantos termos você quer mostrar a mais? "))
print("Fim")
