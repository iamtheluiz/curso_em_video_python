# imports

print("""
|******************|
|    Desafio079    |
|******************|
""")
print("Lista de Números Infinita")
print("")

# Variáveis
nums = []

# Usuário digita os números
while True:
    num = int(input("Digite um número inteiro: "))
    if num not in nums:
        print("Valor Adicionado!")
        nums.append(num)
    else:
        print("Valor já foi adicionado anteriormente!")

    # Deseja continuar?
    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

# Organiza os números em ordem crescente
nums.sort()

print(f"Você digitou os valores {nums}")