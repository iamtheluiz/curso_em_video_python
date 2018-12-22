# imports

print("""
|*****************|
|    Desafio31    |
|*****************|
""")
print("Cobrador de viagens")

km = float(input("Digite a distância em km's para o lugar onde você irá: "))

if km <= 200:
    preco = km*0.5
else:
    preco = km*0.45

print()
print("Sua viagem de {}km vai custar R$ {:.2f}!".format(km, preco))
