# imports

print("""
|******************|
|    Desafio089    |
|******************|
""")
print("Lista de Alunos e suas 2 notas")
print()

# Variáveis
alunos = []
qt_notas = 2

while True:
    # Dados do aluno
    notas = []
    nome = input("Nome: ")

    # Notas do aluno
    for c in range(0, qt_notas):
        notas.append(float(input(f"Nota {c+1}: ")))

    # Armazena os valores
    dados = [nome[:], notas[:]]
    alunos.append(dados[:])

    continuar = ""
    while continuar != "N" and continuar != "S":
        continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar == "N":
        break

print('-='*25)
# Exibe tabela de alunos 21
print("Nº. NOME                  Média")
print("-"*40)
for c, aluno in enumerate(alunos):
    print(f"{c:<3} {aluno[0]:<21} {sum(aluno[1]) / qt_notas}")
print("-"*40)

# Questiona se o usuário deseja ver as notas de um aluno
while True:
    aluno = input("Mostrar notas de qual aluno? ['N' interrompe] x")

    if aluno == 'N':
        break
    else:
        aluno = int(aluno)
        try:
            print(f"Notas de {alunos[aluno][0]} são: {alunos[aluno][1]}")
        except:
            print("O índice desse aluno não existe!")
        print("-" * 40)

print('-='*25)
print("Programa Finalizado!")
