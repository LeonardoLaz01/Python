def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumento(num, taxa):
    aumento = (taxa / 100) * num
    return num + aumento


def diminuir(num, taxa):
    diminuir = (taxa / 100) * num
    return num - diminuir


def moeda(conv):
    return f'R${conv:.2f}'.replace('.', ',')
