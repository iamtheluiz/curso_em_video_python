# imports

print("""
|*****************|
|    Desafio24    |
|*****************|
""")
print("A cidade começa com 'Santo'?")

cidade = input("Digite o nome da cidade: ")
cidade = cidade.lower()
find = cidade.find("santo", 0, 5)
retorno = 0

cidade = cidade.title()

if find == 0:
    retorno = "A cidade '"+cidade+"' começa com a palavra 'SANTO'"
else:
    retorno = "A cidade '"+cidade+"' não começa com a palavra 'SANTO'"

print()
print(retorno)
