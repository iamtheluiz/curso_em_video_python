# imports
from datetime import datetime

print("""
|******************|
|    Desafio041    |
|******************|
""")
print("Categorizando Atletas de Natação")

ano_nasc  = int(input("Digite o ano de nascimento do Atleta: "))
ano_atual = datetime.now().year
idade     = ano_atual - ano_nasc

print()
if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Sênior"
elif idade > 20:
    categoria = "Master"
else:
    categoria = "Padrão"
    print("Ocorreu um problema com a categoria!")

print("O Atleta tem {} anos e está na categoria {}!".format(idade, categoria))
