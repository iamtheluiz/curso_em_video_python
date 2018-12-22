# imports

print("""
|*****************|
|    Desafio26    |
|*****************|
""")
print("Analisador de Frase")

frase = input("Digite uma frase: ")
frase = frase.lower()

count = frase.count("a")
f_a = frase.find("a")
l_a = frase.rfind("a")

print("""
A frase '{}' possuí:
{} letra(s) 'A'
O primeiro 'A' está na {}ª posição
O ultimo 'A' está na {}ª posição
""".format(frase, count, f_a+1, l_a+1))
