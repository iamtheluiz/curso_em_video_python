# imports

print("""
|******************|
|    Desafio063    |
|******************|
""")
print("Sequência de Fibonaci")
print()

nums = int(input("Quantos números da sequência você deseja ver? "))

# Guarda os números da sequência
ant1 = 0  # mais antigo
ant2 = 0  # mais recente
retorno = ""

c = 1
while c <= nums:
    if ant2 == 0:
        retorno = "1"
        ant2 = 1
    else:
        retorno += " -> "+str(ant2 + ant1)
        pote = ant2
        ant2 += ant1
        ant1 = pote

    c += 1

print(retorno)
