# imports

print("""
|******************|
|    Desafio064    |
|******************|
""")
print("Quantos números!")
print()

rodando   = True
digitados = 0
soma      = 0

while rodando:
    num = int(input("Digite um número inteiro: "))

    if num == 999:
        rodando = False
    else:
        digitados += 1
        soma      += num

print("O programa recebeu {} números".format(digitados))
print("A soma desses números resultou em {}".format(soma))
