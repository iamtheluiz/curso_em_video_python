# imports
from datetime import datetime

print("""
|******************|
|    Desafio054    |
|******************|
""")
print("Contador de maioridade")

maiores = 0
menores = 0
ano_atual = datetime.now().year

for i in range(0,7):
    nasc = int(input("Qual o ano de nascimento da {}ª pessoa? ".format(i+1)))
    idade = ano_atual - nasc

    if idade >= 21:
        # É considerado maior
        maiores += 1
    else:
        menores += 1

print()
print("De 7 pessoas:")
print("{} são maiores de idade".format(maiores))
print("{} são menores de idade".format(menores))

