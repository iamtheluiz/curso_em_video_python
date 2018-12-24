# imports

print("""
|******************|
|    Desafio062    |
|******************|
""")
print("Melhorando a PA!")
print()

pt = float(input("Informe o primeiro termo da PA: "))
r  = float(input("Informe a razão da PA: "))

print("Primeiro Termo: {}".format(pt))
print("Razão da PA   : {}".format(r))
c        = 1
termos   = 10
executar = True

while executar:
    while c <= termos:
        print("{}º Termo = {}".format(c, pt + (c - 1) * r))
        c += 1

    qt_mais = int(input("Quantos termos mais você deseja ver? "))

    if qt_mais != 0:
        termos += qt_mais
    else:
        executar = False

print("Acabou o programa!")
