# imports

print("""
|******************|
|    Desafio090    |
|******************|
""")
print("Situação do Aluno")
print()

# Variáveis
aluno = {}
aluno['nome'] = input("Nome: ")
aluno['média'] = float(input("Média: "))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print("-="*25)
for k, v in aluno.items():
    print(f'{k.title()} => {v}')
