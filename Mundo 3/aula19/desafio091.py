# imports
from time import sleep
from random import randint
from operator import itemgetter

print("""
|******************|
|    Desafio091    |
|******************|
""")
print("4 Jogadores... 1 Dado")
print()

# Variáveis
jogo = {}

print("=== Sorteio ===")
for i in range(1, 5):
    dado = randint(1, 6)
    jogo['jogador_'+str(i)] = dado
    sleep(0.5)
    print(f'O jogador {i} tirou {dado}')

print("=== Ranking ===")
i = 1
for chave, valor in sorted(jogo.items(), key=itemgetter(1), reverse=True):
    chave = chave.replace("_", " ").title()
    print(f'{i}º Lugar => {chave} tirando {valor}')
    i += 1
