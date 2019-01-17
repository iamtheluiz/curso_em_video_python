# imports

print("""
|******************|
|    Desafio084    |
|******************|
""")
print("Pessoas e seus pesos")
print()

# Variáveis
pessoas = []
pessoa = []
maior_peso = 0
lista_maior = []
menor_peso = 0
lista_menor = []

while True:
    # Inputs do usuário
    pessoa.append(input("Nome da pessoa: "))
    pessoa.append(float(input("Peso da pessoa: ")))

    # Lista com pessoas mais pesadas
    if maior_peso == 0 or pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
        lista_maior.clear()
        lista_maior.append(pessoa[0])
    elif maior_peso == pessoa[1]:
        lista_maior.append(pessoa[0])

    # Lista com pessoas mais leves
    if menor_peso == 0 or pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
        lista_menor.clear()
        lista_menor.append(pessoa[0])
    elif menor_peso == pessoa[1]:
        lista_menor.append(pessoa[0])

    # Adiciona na lista geral
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

# Exibe os resultados
print('-='*20)
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'As pessoas mais pesadas foram {lista_maior} com {maior_peso} kg')
print(f'As pessoas mais pesadas foram {lista_menor} com {menor_peso} kg')