num = int(input('Número: '))
primo = 0
for c in range(1, num+1):
    conta = num % c
    if conta == 0:
        primo = primo + c
if primo == num + 1:
    print(f'{num} é primo.')
else:
    print(f'{num} não é primo.')