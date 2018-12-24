# imports

print("""
|******************|
|    Desafio056    |
|******************|
""")
print("Informações de 4 pessoas")
print()

soma_idade  = 0
homem_old   = "SEM HOMENS NA LISTA"
idade_old   = 0
mulheres_lv = 0 # Mulheres com menos de vinte anos
for i in range(0, 4):
    print("======= {}ª Pessoa =======".format(i+1))
    nome = input("Digite o nome da {}ª pessoa: ".format(i+1))
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i + 1)))
    sexo = input("Digite o sexo da {}ª pessoa (M ou F): ".format(i + 1))
    sexo = sexo.upper()

    soma_idade += idade

    if sexo == "M":
        if idade_old == 0 or idade > idade_old:
            idade_old = idade
            homem_old = nome
    elif sexo == "F":
        if idade < 20:
            mulheres_lv += 1

# Calcula a media da idade
media_idade = soma_idade / 4

print("Das 4 pessoas:")
print("A média das idades é {} anos".format(media_idade))
if(idade_old == 0):
    print("Não existem homens na lista")
else:
    print("Homem mais velho: {}".format(homem_old))
print("Existem {} mulheres com menos de 20 anos".format(mulheres_lv))

