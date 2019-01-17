# imports

print("""
|******************|
|    Desafio086    |
|******************|
""")
print("Matriz 3x3")
print()

# Variáveis
matriz = [
    [],
    [],
    []
]

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Digite um número inteiro para [{c}, {i}]: "))
        matriz[c].insert(i, num)

print('-='*20)
for c in range(0, 3):
    for i in range(0, 3):
        if i != 2:
            print(f"[{matriz[c][i]:^7}]", end="")
        else:
            print(f"[{matriz[c][i]:^7}]")
