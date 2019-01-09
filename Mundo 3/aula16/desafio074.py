# imports
from random import randint

print("""
|******************|
|    Desafio074    |
|******************|
""")
print("Números Aleatórios!")

# Variáveis
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
nums    = ""    # String com os números sorteados
maior   = ""
menor   = ""

# Faz as verificações
for i, num in enumerate(numeros):
    # Faz a lista de números
    if i < 4 and i != 0:
        nums += ", "
    elif i == 4:
        nums += " e "
    nums += str(num)

    # Verifica se é o maior
    if str(maior) == "" or num > maior:
        maior = num

    # Verifica se é o menor
    if str(menor) == "" or num < menor:
        menor = num

print("=======================================================")
print(f"Os números selecionados foram: {nums}")
print(f'O menor número gerado foi {menor}')
print(f'O maior número gerado foi {maior}')
