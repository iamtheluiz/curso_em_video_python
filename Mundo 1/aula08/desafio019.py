# imports
from random import randint

print("|*****************|")
print("|    Desafio19    |")
print("|*****************|")
print("")
print("Sorteador de alunos (4 alunos)")

contador = 0
alunos = []

while contador <= 3:
    alunos.append(input("Digite o nome do aluno: "))
    contador += 1

random = randint(0, 3)

print()
print("O aluno escolhido foi {}!".format(alunos[random]))
