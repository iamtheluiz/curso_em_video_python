# imports
from random import randint
from time import sleep

print("""
|******************|
|    Desafio100    |
|******************|
""")
print("Soma dos pares sorteados!")
print()

# Variáveis
lista = []


# Funções
def sorteia():
    lista.clear()
    print("="*35)
    print("Sorteando 5 valores... ", end="")
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        sleep(0.4)
        print(f"{num} ", end="", flush=True)

    print("PRONTO!")


def somaPar():
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Código Principal
while True:
    sorteia()
    somaPar()

    # Mais uma vez?
    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja sortear novamente? [S/N] ").upper()

    if continuar == "N":
        break
