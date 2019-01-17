# imports

print("""
|******************|
|    Desafio083    |
|******************|
""")
print("Expressão matemática")
print()

# Variáveis
exp = input("Digite a expressão: ")
parenteses = []

for char in exp:
    if char == "(":
        parenteses.append("(")
    elif char == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break

if len(parenteses) == 0:
    print("A expressão é válida!")
else:
    print("Expressão inválida!")
