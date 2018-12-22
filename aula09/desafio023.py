# imports

print("""
|*****************|
|    Desafio23    |
|*****************|
""")
print("Contador de Unidades")

num = int(input("Digite um número entre 0 e 99999: "))
num = str(num)

unidades = ['unidade', 'dezena', 'centena', 'unidade de milhar', 'dezena de milhar']
contador = len(num) - 1

print()
while contador >= 0:
    print("{}: {}".format(unidades[contador],num[contador]))
    contador -= 1
