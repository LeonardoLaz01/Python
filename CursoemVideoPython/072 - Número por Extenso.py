numeros = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar == 'S':
            continue
        if continuar == 'N':
            print('fim do programa')
            break
