# imports

print("""
|******************|
|    Desafio095    |
|******************|
""")
print("Aproveitamento - Jogador de Futebol v2.0")
print()

# Variáveis
jogadores = []
jogador = {}

while True:
    jogador.clear()
    print("-"*40)
    # Nome
    jogador["nome"] = input("Nome do jogador: ")
    # Quantidade de partidas
    jogador["partidas_jogadas"] = int(input(f"Partidas que {jogador['nome']} jogou: "))
    # Gols em cada uma das partidas
    jogador["gols"] = []
    for i in range(0, jogador["partidas_jogadas"]):
        jogador["gols"].append(int(input(f"   Gols na partida {i+1}: ")))
    # Total de Gols
    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())

    # Deseja continuar?
    continuar = ""
    while continuar not in ['N', 'S']:
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

# Exibição
print("-="*32)
print("Código  Nome"+" "*45+" Total ")
print("-"*64)
for cod, jogador in enumerate(jogadores):
    print(f'{cod:>7} ', end='')
    print(f'{jogador["nome"]:<49} ', end='')
    print(f'{jogador["total"]}')

# Verifica se o usuário deseja ver o aproveitamento de um jogador específico
while True:
    print("-=" * 25)
    codigo = input("Mostrar aproveitamento de qual jogador? [N para cancelar] ")
    if codigo.isnumeric():
        codigo = int(codigo)
        if codigo >= len(jogadores):
            print("O código do jogador não é válido!!")
        else:
            print("-=" * 32)
            print(f"O jogador {jogador['nome']} jogou {jogador['partidas_jogadas']} partidas!")
            for i, valor in enumerate(jogador["gols"]):
                print(f"  => Na partida {i + 1}, fez {valor} gols.")
            print(f"Foi um total de {jogador['total']} gols")
    elif codigo == "N":
        break
    else:
        print("Digite um valor válido!")
