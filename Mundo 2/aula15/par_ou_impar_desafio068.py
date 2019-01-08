# imports
from random import randint

print("""
|******************|
|    Desafio068    |
|******************|
""")
print("Par Ou Ímpar!")

print("""
===========================
 Vamos Jogar Par ou Ímpar!
===========================
""")

# "Globais"
vitorias = 0
derrota  = False

while True:
    # Usuário faz suas escolhas
    num     = int(input("Digite um número: "))
    escolha = ""

    while escolha != "P" and escolha != "I":
        escolha = input("Par ou Ímpar? (P ou I) ").upper()

    # PC escolhe um número
    pc_num = randint(0, 10)

    # Verifica se é par ou impar
    soma = pc_num + num
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"

    # Verifica o ganhador
    if resultado == "PAR" and escolha == "P":
        # Jogador venceu
        vitorias += 1
    elif resultado == "ÍMPAR" and escolha == "I":
        # Jogador venceu
        vitorias += 1
    else:
        # Jogador perdeu
        derrota = True

    if not derrota:
        print("---------------------------------------------")
        print(f"Você jogou {num} e o computador {pc_num}. Total de {soma} DEU {resultado}")
        print("---------------------------------------------")
        print("Você VENCEU!!")
        print("Vamos para mais uma rodada!")
    else:
        print("---------------------------------------------")
        print(f"Você jogou {num} e o computador {pc_num}. Total de {soma} DEU {resultado}")
        print("---------------------------------------------")
        print("Você PERDEU...")
        break

print("{}=".format("=-"*15))
print(f"Você venceu {vitorias} vezes!")