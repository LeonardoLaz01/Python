print(15 * '-=')
print('Analisador de Triângulos')
print(15 * '-=')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
calc1 = a + b
calc2 = a + c
calc3 = b + c
if calc1 > c and calc2 > b and calc3 > a:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
