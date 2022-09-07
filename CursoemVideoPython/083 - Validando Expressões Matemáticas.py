expressao = input('Digite a expressão: ')
pilha = list()
for letra in expressao:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
if len(pilha) <= 0:
    print('Expressão válida')
else:
    print('Expressão está errada')
