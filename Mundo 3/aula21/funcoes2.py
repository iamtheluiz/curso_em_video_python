def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Início da Contagem
    :param f: Fim da Contagem
    :param p: Passo da Contagem
    :return: Sem retorno
    Luiz Gustavo da Silva Vasconcellos
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print("FIM!")


contador(2, 10, 2)
help(contador)

print("="*35)
print(f'{"SOMA":^35}')
print("="*35)


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro Valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    Luiz Gustavo da Silva Vasconcellos
    """
    s = a+b+c
    print(f'A soma vale {s}!')


somar(8, 4)
somar()

print("="*35)
print(f'{"ESCOPO DE VARIÁVEL":^35}')
print("="*35)


def teste():
    n = 1   # Variável "n" local (diferente da global)
    x = 8   # Escopo Local (só funciona dentro da função)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2   # Escopo Global (Funciona de maneira global)
teste()
print(f'No Programa Principal, n vale {n}')
# print(f'Na Programa Principal, x vale {x}')

print('-'*35)


def teste():
    global n    # Usa o 'n' do escopo global
    n = 1   # Altera o 'n' global
    x = 8   # Escopo Local (só funciona dentro da função)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2   # Escopo Global (Funciona de maneira global)
teste()
print(f'No Programa Principal, n vale {n}')

print("="*35)
print(f'{"RETORNO":^35}')
print("="*35)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


print(f'A soma vale {somar(3, 2, 5)}')
r1 = somar(1, 7)
r2 = somar(2, 6, 8)
print(f'Os resultados foram {r1} e {r2}')

print("="*35)
print(f'{"FATORIAL - CALCULO":^35}')
print("="*35)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
