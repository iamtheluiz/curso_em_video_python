teste = []
teste.append("Luiz")
teste.append(17)
galera = []
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

print("-="*20)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
for i, pessoa in enumerate(galera):
    print(f'Pessoa {i+1}: {pessoa[0]} com {pessoa[1]} anos')

print("-="*20)
galera = []
dados = []

while True:
    dados.append(input("Digite o nome da pessoa: "))
    dados.append(input("Digite a idade dela: "))

    # Armazena na galera
    galera.append(dados[:])
    dados.clear()

    continuar = ""
    while continuar != "S" and continuar != "N":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

print(galera)

