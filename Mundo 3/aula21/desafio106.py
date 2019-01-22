# imports

print("""
|******************|
|    Desafio106    |
|******************|
""")


# Funções
def getComando():
    comando = input("Função ou Biblioteca > ")

    if comando == 'fim':
        return False

    titulo(f"Acessando o manual do comando '{comando}'", 'azul')
    print('\033[1;7;30m')
    print(help(comando))
    print('\033[m', end='')

    return True


def titulo(text, cor):
    if cor == 'azul':
        print('\033[44;30m', end='')
    elif cor == 'vermelho':
        print('\033[41;30m', end='')
    elif cor == 'verde':
        print('\033[42;30m', end='')
    elif cor == 'branco':
        print('\033[1;7;30m', end='')
    else:
        print('\033[m', end='')

    tamanho = len(text) + 4
    print("="*tamanho)
    print(f'{text:^{tamanho}}')
    print("=" * tamanho)
    print('\033[m', end='')


titulo("SISTEMA DE AJUDA 'PyHELP'", "verde")
while True:
    retorno = getComando()

    if not retorno:
        titulo("ATÉ MAIS!", "vermelho")
        break
