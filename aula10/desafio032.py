# imports

print("""
|*****************|
|    Desafio33    |
|*****************|
""")
print("Ano bissexto?")

ano = int(input("Digite um ano: "))
retorno = ""

print()
if ano % 4 == 0:
    if ano % 100 != 0:
        retorno = "O ano de "+str(ano)+" é bissexto!"
    else:
        if ano % 400 == 0:
            retorno = "O ano de " + str(ano) + " é bissexto!"
        else:
            retorno = "O ano de "+str(ano)+" não é bissexto!"
else:
    if ano % 400 == 0:
        retorno = "O ano de " + str(ano) + " é bissexto!"
    else:
        retorno = "O ano de " + str(ano) + " não é bissexto!"



print(retorno)
