# imports

print("""
|******************|
|    Desafio075    |
|******************|
""")
print("Os quatro valores!")

# Variáveis
nums = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
valores = ""
vl_pares = ""

# Faz uma lista "bonita"
for pos, num in enumerate(nums):
    if pos < 3 and pos != 0:
        valores += ", "
    elif pos == 3:
        valores += " e "
    valores += str(num)

    # Verifica se o valor é par
    if num % 2 == 0:
        vl_pares += " "+str(num)

print("=========================================================================")
print(f"Os números digitados foram: {valores}")
if 9 in nums:
    print(f"O número 9 apareceu {nums.count(9)} vezes")
else:
    print("O número 9 não foi digitado!")

if 3 in nums:
    print(f"O número 3 apareceu pela primeira vez na {nums.index(3) + 1} posição!")
else:
    print("O número 3 não foi digitado!")
print(f"Foram digitados os seguintes números pares: {vl_pares}")
