# imports

print("""
|******************|
|    Desafio102    |
|******************|
""")
print("Calculo de Fatorial")
print()


# Funções
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número
    :param num: O número a ser calculado
    :param show: Mostra ou não a conta (opcional)
    :return: Retorna o valor do Fatorial de 'num'
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if c == num:
            ret = f'{num} '
        else:
            ret += f'x {c} '
    ret += f'= {f}'
    if show:
        return ret
    else:
        return f


print(fatorial(5, True))
print(fatorial(5, False))
print(fatorial(5))
