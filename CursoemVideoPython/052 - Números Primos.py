# Verificador de número primo
num = int(input('Número: '))
primo = 0
for c in range(1, num+1):
    conta = num % c  # Verificando por quais números o valor inserido é divisível
    if conta == 0:
        primo = primo + c  # Contando por quantos números ele foi divisível
if primo == num + 1:
    print(f'{num} é primo.')  # Divisível apenas por 1 e ele mesmo
else:
    print(f'{num} não é primo.')  # Divisível por mais números
