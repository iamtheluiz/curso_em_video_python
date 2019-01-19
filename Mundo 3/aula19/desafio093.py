# imports

print("""
|******************|
|    Desafio093    |
|******************|
""")
print("Aproveitamento - Jogador de Futebol")
print()

# Variáveis
jogador = {}

# Nome
jogador["nome"] = input("Nome do jogador: ")
# Quantidade de partidas
jogador["partidas_jogadas"] = int(input(f"Partidas que {jogador['nome']} jogou: "))
# Gols em cada uma das partidas
jogador["gols"] = []
for i in range(0, jogador["partidas_jogadas"]):
    jogador["gols"].append(int(input(f"Gols na partida {i+1}: ")))
# Total de Gols
jogador["total"] = sum(jogador["gols"])

# Exibição
print("-="*25)
print(jogador)
print("-="*25)
print(f"Nome: {jogador['nome']}")
print(f"Gols: {jogador['gols']}")
print(f"Total de Gols: {jogador['total']}")
print("-="*25)
print(f"O jogador {jogador['nome']} jogou {jogador['partidas_jogadas']} partidas!")
for i, valor in enumerate(jogador["gols"]):
    print(f"  => Na partida {i+1}, fez {valor} gols.")
print(f"Foi um total de {jogador['total']} gols")
