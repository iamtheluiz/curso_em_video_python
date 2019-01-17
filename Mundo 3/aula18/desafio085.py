# imports

print("""
|******************|
|    Desafio085    |
|******************|
""")
print("7 Valores Numéricos")
print()

# Variáveis
nums = [[], []]

for c in range(0, 7):
    num = int(input(f"Digite o {c+1}º número inteiro: "))
    if num % 2 == 0:
        # Par
        nums[0].append(num)
    else:
        # Impar
        nums[1].append(num)

# Ordena
nums[0].sort()
nums[1].sort()

print('-='*20)
print(f'Os valores pares digitados foram: {nums[0]}')
print(f'Os valores ímpares digitados foram: {nums[1]}')
