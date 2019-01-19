# imports

print("""
|******************|
|    Desafio094    |
|******************|
""")
print("Cadastro de Pessoas")
print()

# Variáveis
pessoas = list()
pessoa  = dict()
m_idade = 0

while True:
    pessoa.clear()
    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = ""
    while pessoa["sexo"] != "M" and pessoa["sexo"] != "F":
        pessoa["sexo"] = input("Sexo [M/F]: ").upper()
    pessoa["idade"] = int(input("Idade: "))
    m_idade += pessoa["idade"]
    pessoas.append(pessoa.copy())

    # Questiona o usuário sobre continuar
    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

# Calcula a média da idade
m_idade = m_idade/len(pessoas)

print("-="*25)
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'A idade média do grupo é {m_idade:.2f} anos!')
print('As mulheres cadastradas foram: ')
for pessoa in pessoas:
    if pessoa["sexo"] == "F":
        print(f'  > {pessoa["nome"]}, {pessoa["idade"]} - {pessoa["sexo"]}')
print('Pessoas acima da idade média: ')
for pessoa in pessoas:
    if pessoa["idade"] > m_idade:
        print(f'  > {pessoa["nome"]}, {pessoa["idade"]} - {pessoa["sexo"]}')
