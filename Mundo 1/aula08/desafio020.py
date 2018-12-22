# imports
from random import randint

print("|*****************|")
print("|    Desafio20    |")
print("|*****************|")
print("")
print("Ordenador de Alunos (4 alunos)")

contador = 0
alunos = []
ordem = []

while contador <= 3:
    alunos.append(input("Digite o nome do aluno: "))
    contador += 1

while len(alunos) > 0:
    random = randint(0, len(alunos) - 1)
    ordem.append(alunos[random])
    alunos.pop(random)

print()
print("Ordem sorteada: ")
contador = 1
while len(ordem) > 0:
    print("{}º -> {}".format(contador, ordem[0]))
    ordem.pop(0)
    contador += 1
