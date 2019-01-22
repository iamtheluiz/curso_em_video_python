# imports

print("""
|******************|
|    Desafio103    |
|******************|
""")
print("Ficha de Jogador")
print()


# Funções
def ficha(nome="", gols=""):
    """
    -> Mostra a ficha de um jogador
    :param nome: Nome do Jogador
    :param gols: Quantidade de gols feitos no campeonato
    :return: Ficha do Jogador
    """
    if nome.strip() == "":
        nome = "<desconhecido>"
    if not gols.isnumeric():
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


# Dados
nome = input("Nome de Jogador: ")
gols = input("Quantidade de gols marcados: ")
print(ficha(nome, gols))
