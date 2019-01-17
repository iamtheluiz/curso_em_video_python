# imports

print("""
|******************|
|    Desafio081    |
|******************|
""")
print("Lista de Números")
print()

# Variáveis
nums = []

# Input do usuário
while True:
    nums.append(int(input("Digite um número inteiro: ")))

    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

nums.sort(reverse=True)

print("-="*20)
print(f'Foram digitados {len(nums)} números!')
print(f'A lista ordenada de forma decrescente: {nums}')
if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')

