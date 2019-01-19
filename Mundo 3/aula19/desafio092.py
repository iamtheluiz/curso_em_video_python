# imports
from datetime import date

print("""
|******************|
|    Desafio092    |
|******************|
""")
print("Dados CTPS")
print()

# Variáveis
pessoa = {}

# Questiona o nome
pessoa["nome"] = input("Seu nome: ")
# Ano de nascimento
ano = int(input("Ano de nascimento: "))
pessoa["idade"] = date.today().year - ano   # Calcula a idade
# Carteira de trabalho
pessoa["ctps"] = input("Carteira de trabalho (0 caso não tenha): ")

# Verifica se foi passado um número de CTPS
if pessoa["ctps"] != "0":
    # Ano de contratação
    pessoa["ano_de_contratacao"] = input("Ano de contratação: ")
    # Salário
    pessoa["salário"] = float(input("Salário: "))
    # Verifica a aposentadoria (considerando 35 anos de colaboração)
    pessoa["aposentadoria"] = 35 - (date.today().year - int(pessoa["ano_de_contratacao"])) + int(pessoa["idade"])

# Exibe os dados
print("-="*25)
for key, value in pessoa.items():
    key = key.replace("_", " ").title()
    print(f'{key} => {value}')
