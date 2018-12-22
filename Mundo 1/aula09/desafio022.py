# imports

print("""
|*****************|
|    Desafio22    |
|*****************|
""")
print("Transformação do Nome")

nome = input("Digite seu nome completo: ")

upper = nome.upper()
lower = nome.lower()
qt_letras = len("".join(nome.split()))
qt_first = len(nome.split()[0])

print("""
Nome: {}
Todo maiúsculo: {}
Todo minúsculo: {}
Quantidade de letras: {}
Letras do primeiro nome: {}
""".format(nome, upper, lower, qt_letras, qt_first))
