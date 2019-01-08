# imports

print("""
|******************|
|    Desafio069    |
|******************|
""")
print("Analise de Várias Pessoas!")

# Variáveis
nr_maiores     = 0  # Maiores de idade
nr_homens      = 0  # Homens cadastrados
nr_mulheres_lv = 0  # Mulheres com menos de 20 anos

while True:

    print("===================")
    print("Cadastre uma pessoa")
    print()
    # Questiona a idade
    idade = int(input("Idade: "))

    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = input("Sexo (M ou F): ").upper()

    # Faz as contagens
    if idade >= 18:
        nr_maiores += 1

    if sexo == "M":
        nr_homens += 1
    elif sexo == "F" and idade < 20:
        nr_mulheres_lv += 1

    print("--------------------")
    escolha = ""
    while escolha != "S" and escolha != "N":
        escolha = input("Deseja continuar? (S ou N) ").upper()

    if escolha == "N":
        break

print("==== Fim Do Programa ====")
print(f"Pessoas com mais de 18 anos {nr_maiores}")
print(f"Existem {nr_homens} homens cadastrados!")
print(f"Existem {nr_mulheres_lv} mulheres com menos de 20 anos cadastradas!")
