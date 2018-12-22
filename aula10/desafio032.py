# imports
from datetime import datetime

print("""
|*****************|
|    Desafio33    |
|*****************|
""")
print("Ano bissexto?")

ano = int(input("Digite um ano (digite 0 para considerar o atual): "))
retorno = ""

if ano == 0:
    ano = datetime.now().year

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
