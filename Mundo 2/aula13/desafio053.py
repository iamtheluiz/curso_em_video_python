# imports

print("""
|******************|
|    Desafio053    |
|******************|
""")
print("A frase é um palíndromo?")

frase = str(input("Digite uma frase: "))
original = frase

frase = frase.upper()
frase = frase.split()
frase = "".join(frase)

frase_reverse = ""
# Gera frase invertida
for i in range(len(frase)-1, -1, -1):
    frase_reverse += frase[i]

if frase_reverse == frase:
    # É um palíndromo
    print("A frase '{}' É um palíndromo!".format(original))
else:
    # Não é um palíndromo
    print("A frase '{}' NÃO é um palíndromo!".format(original))
