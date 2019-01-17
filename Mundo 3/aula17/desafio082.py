# imports

print("""
|******************|
|    Desafio082    |
|******************|
""")
print("Lista Total, lista de pares e lista de impares")
print()

# Variáveis
nums = []
pares = []
impares = []

while True:
    nums.append(int(input("Digite um número inteiro: ")))

    continuar = ""
    while continuar != "S" and continuar != "N":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

# Ao terminar, faz uma lista com números pares e impares
for num in nums:
    if num % 2 == 0:
        # Número par
        pares.append(num)
    else:
        # Número impar
        impares.append(num)

print("-="*20)
print(f'A lista completa é {nums}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números impares é {impares}')
