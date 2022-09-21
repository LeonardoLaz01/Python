def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
          print(f'{i}', end=' x ')
    return f'{f}'

print('-' * 40)
print(fatorial(5, True))
help(fatorial)