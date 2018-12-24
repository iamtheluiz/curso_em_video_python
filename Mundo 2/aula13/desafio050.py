# imports

print("""
|******************|
|    Desafio050    |
|******************|
""")
print("Soma dos números inteiros pares que o usuário digitar")

soma   = 0
result = ""
for c in range(0, 6):
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0:
        soma += num
        if result == "":
            result += str(num)
        else:
            result += ", "+str(num)

print("A soma entre {} resultou em {}".format(result, soma))