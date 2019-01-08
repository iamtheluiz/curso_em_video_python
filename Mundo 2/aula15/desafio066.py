# imports

print("""
|******************|
|    Desafio066    |
|******************|
""")
print("Soma dos Números")
print()

soma = 0
digitados = 0
while True:
    num = int(input("Digite um número: (999 para) "))
    if num == 999:
        break
    soma += num
    digitados += 1

print(f"A soma dos {digitados} valores é {soma}")
