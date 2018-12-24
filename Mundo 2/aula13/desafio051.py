# imports

print("""
|******************|
|    Desafio051    |
|******************|
""")
print("Calculo de PA")

pt = float(input("Digite o primeiro termo da progressão: "))
r  = float(input("Digite a razão da progressão: "))

print()
print("Razão: {}".format(r))
for i in range(0, 10):
    print("{}º termo = {}".format(i+1, pt + ((i) * r)))
