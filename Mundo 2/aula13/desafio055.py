# imports

print("""
|******************|
|    Desafio055    |
|******************|
""")
print("Maior e Menor Peso")

maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input("Digite o {}º peso (kg): ".format(i+1)))

    # Verifica se é o maior
    if peso > maior or maior == 0:
        maior = peso

    # Verifica se é o menor
    if peso < menor or menor == 0:
        menor = peso

print("Dos 5 pesos digitados:")
print("O maior é {} kg".format(maior))
print("O menor é {} kg".format(menor))
