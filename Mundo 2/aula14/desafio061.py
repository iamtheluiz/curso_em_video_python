# imports

print("""
|******************|
|    Desafio061    |
|******************|
""")
print("PA!")
print()

pt = float(input("Informe o primeiro termo da PA: "))
r  = float(input("Informe a razão da PA: "))

print("Primeiro Termo: {}".format(pt))
print("Razão da PA   : {}".format(r))
c = 1
while c <= 10:
    print("{}º Termo = {}".format(c, pt + (c - 1) * r))
    c += 1