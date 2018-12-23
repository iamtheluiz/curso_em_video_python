# imports

print("""
|******************|
|    Desafio042    |
|******************|
""")
print("Categorizando Triângulos")

l1 = float(input("Digite o valor do primeiro lado: "))
l2 = float(input("Digite o valor do segundo lado : "))
l3 = float(input("Digite o valor do terceiro lado: "))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    # Pode formar um triângulo

    # Verifica que tipo de triângulo é
    if l1 == l2 and l2 == l3:
        # Triângulo Equilátero
        categoria = "Equilátero"
    elif l1 == l2 or l2 == l3 or l3 == l1:
        # Triângulo Isósceles
        categoria = "Isósceles"
    else:
        # Triângulo Escaleno
        categoria = "Escaleno"

    print("O triângulo formado pelos lados {}, {} e {} é {}".format(l1, l2, l3, categoria))

else:
    # Não forma um triângulo
    print("Não é possível formar um triângulo com os lados {}, {} e {}".format(l1, l2, l3))
