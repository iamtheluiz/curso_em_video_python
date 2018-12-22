# imports

print("""
|*****************|
|    Desafio25    |
|*****************|
""")
print("O seu nome possuí 'Silva'?")

nome = input("Digite seu nome: ")
nome = nome.lower()
counter = nome.count("silva")
nome = nome.title()

if counter != 0:
    retorno = "Seu nome possuí o nome 'Silva'!"
else:
    retorno = "Seu nome não possuí o nome 'Silva'!"

print()
print("Seu nome: {}".format(nome))
print(retorno)
