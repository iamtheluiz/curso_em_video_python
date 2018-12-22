# imports

print("""
|*****************|
|    Desafio27    |
|*****************|
""")
print("Separador de Nomes")

nome = input("Digite seu nome completo: ")
nome = nome.split()

print("""
Nome completo: {}
Primeiro nome: {}
Ultimo nome  : {}
""".format(" ".join(nome), nome[0], nome[len(nome) - 1]))
