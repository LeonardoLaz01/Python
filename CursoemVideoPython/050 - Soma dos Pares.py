# Soma de Seis Valores Pares
s = 0
q = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))  # Valores
    if n % 2 == 0:  # Verificando se é par
        s = s + n
        q = q + 1
print(f'Você informou {q} números pares e a soma entre eles é {s}')
