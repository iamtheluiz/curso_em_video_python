# imports

print("""
|******************|
|    Desafio037    |
|******************|
""")
print("Conversão Numérica")

num = int(input("Digite um número: "))

escolha = False
while not escolha:
    base = int(input("Você deseja converte-lo para qual base? 1-Binário, 2-Octal e 3-Hexadecimal "))
    escolha = True
    if base == 1:
        tipo = "Binário"
        result = bin(num)[2:]
    elif base == 2:
        tipo = "Octal"
        result = oct(num)[2:]
    elif base == 3:
        tipo = "Hexadecimal"
        result = hex(num)[2:]
    else:
        print("Opção inválida. Escolha novamente!")
        escolha = False

print("O número {} em {} é {}".format(num, tipo, result))
