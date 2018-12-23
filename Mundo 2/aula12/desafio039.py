# imports
from datetime import datetime

print("""
|******************|
|    Desafio039    |
|******************|
""")
print("Verificar Alistamento")

ano_nasc  = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.now().year
idade     = ano_atual - ano_nasc

print()
if idade < 18:
    # Ainda não chegou a hora
    print("Você tem {} anos e ainda não está na idade para se alistar!".format(idade))
    print("Faltam {} ano(s) para seu alistamento.".format(18 - idade))
elif idade == 18:
    # Chegou a hora
    print("Você tem 18 anos e está na idade para se alistar!")
elif idade > 18:
    # Passou da hora
    print("Você tem {} anos e já passou da idade para se alistar!".format(idade))
    print("Faz(em) {} ano(s) que você fez ou devia ter feito o alistamento".format(idade - 18))
else:
    print("Ocorreu um erro ao verificar seu alistamento!")
