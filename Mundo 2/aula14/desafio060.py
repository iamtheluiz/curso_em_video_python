# imports

print("""
|******************|
|    Desafio060    |
|******************|
""")
print("Número Fatorial")
print()

num       = int(input("Digite um número: "))
conta     = ""
resultado = 1

i = num
while i >= 1:
    if conta == "":
        conta += str(i)
    else:
        conta += "x"+ str(i)
    resultado = resultado * i
    i -= 1

print("5! = {} = {}".format(conta, resultado))
