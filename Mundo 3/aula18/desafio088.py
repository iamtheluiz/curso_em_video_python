# imports
from random import randint
from time import sleep

print("""
|******************|
|    Desafio088    |
|******************|
""")
print("Palpites da Mega-Sena")
print()

# Variáveis
jogos = []

# Quantidade de jogos
qt_jogos = int(input("Digite quantos jogos você deseja gerar: "))

# Repetição do sistema
for c in range(0, qt_jogos):
    jogo = []
    i = 0
    while i < 6:
        num = randint(1, 60)
        if num not in jogo:
            # Coloca no jogo
            jogo.append(num)
            i += 1

    # Coloca o jogo gerado entre os jogos
    jogo.sort()
    jogos.append(jogo)

# Exibe os jogos gerados
print('-='*20)
for i, jogo in enumerate(jogos):
    print(f'{i+1}º Jogo: {jogo}')
    sleep(0.8)
print('-='*20)
