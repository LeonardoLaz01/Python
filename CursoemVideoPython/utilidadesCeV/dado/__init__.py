def leiadinheiro(msg):
    valor = input(msg).replace(',', '.').strip()
    while True:
        if valor.isalpha() or valor.isspace() or not valor:
            print(f'ERRO: "{valor}" é um preço inválido')
            valor = input(msg).replace(',', '.').strip()
        else:
            return float(valor)
