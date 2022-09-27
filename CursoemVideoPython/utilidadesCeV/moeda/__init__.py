def metade(num, cond=False):
    if cond:
        return moeda(num / 2)
    else:
        return num / 2


def dobro(num, cond=False):
    if cond:
        return moeda(num * 2)
    else:
        return num * 2


def aumento(num, taxa, cond=False):
    aumento = (taxa / 100) * num
    if cond:
        return moeda(num + aumento)
    else:
        return num + aumento


def diminuir(num, taxa, cond=False):
    diminuir = (taxa / 100) * num
    if cond:
        return moeda(num - diminuir)
    else:
        return num - diminuir


def moeda(conv):
    return f'R${conv:.2f}'.replace('.', ',')


def resumo(num, aumnt, dmnr):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aumnt}% de aumento: \t{aumento(num, aumnt, True)}')
    print(f'{dmnr}% de redução: \t{diminuir(num, dmnr, True)}')
    print('-' * 30)