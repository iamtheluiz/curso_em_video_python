# imports

print("""
|*****************|
|    Desafio35    |
|*****************|
""")
print("Esse triângulo existe?")

l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
l2 = float(input("Digite o valor do segundo lado do triângulo: "))
l3 = float(input("Digite o valor do terceiro lado do triângulo: "))

print(l1 + l3)

# Formato da Correção
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    existe = True
else:
    existe = False

# Formato Antigo:
# if (l1 + l2) > l3:
#    if (l1 + l3) > l2:
#        if (l2 + l3) > l1:
#            existe = True
#        else:
#            existe = False
#    else:
#        existe = False
#else:
#    existe = False

if existe:
    print("As retas de tamanho {}, {} e {} podem formar um triângulo!".format(l1, l2, l3))
else:
    print("As retas de tamanho {}, {} e {} não conseguem formar um triângulo!".format(l1, l2, l3))
