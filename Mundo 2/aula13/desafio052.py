# imports

print("""
|******************|
|    Desafio052    |
|******************|
""")
print("Número é primo?")

num = int(input("Digite um número inteiro: "))

divisoes = 0
for i in range(1, num+1):
    if num % i == 0:
        divisoes += 1

# Verifica se dividiu mais de 2 vezes
if divisoes > 2:
    # Não é primo
    print("O número {} não é primo!".format(num))
else:
    # É primo
    print("O número {} é primo!".format(num))
