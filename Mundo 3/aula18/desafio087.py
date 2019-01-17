# imports

print("""
|******************|
|    Desafio087    |
|******************|
""")
print("Matriz 3x3 v2.0")
print()

# Variáveis
matriz = [
    [],
    [],
    []
]
soma_pares = 0

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f"Digite um número inteiro para [{c}, {i}]: "))
        matriz[c].insert(i, num)

        if num % 2 == 0:
            soma_pares += num

print('-='*20)
for c in range(0, 3):
    for i in range(0, 3):
        if i != 2:
            print(f"[{matriz[c][i]:^7}]", end="")
        else:
            print(f"[{matriz[c][i]:^7}]")

print('-='*20)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
matriz[1].sort(reverse=True)
print(f'O maior valor da segunda linha é {matriz[1][0]}')
