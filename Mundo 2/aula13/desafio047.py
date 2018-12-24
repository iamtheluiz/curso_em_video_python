# imports

print("""
|******************|
|    Desafio047    |
|******************|
""")
print("Números Pares de 1 até 50")

result = ""
for i in range(1, 51, 2):
    if i == 1:
        result += str(i + 1)
    else:
        result += ", "+str(i + 1)

print(result)
