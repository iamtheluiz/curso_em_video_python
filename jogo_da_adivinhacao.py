# imports
from random import randint

print("""
|*******************|
|    Adivinhação    |
|*******************|
""")
print("Adivinhe o número (de 0 a 1000)!")

pc_num = randint(0, 1000)
winner = False
jogadas = 0

while not winner:
    u_num = int(input("Digite um número: "))

    if u_num == pc_num:
        winner = True
    else:
        if u_num < pc_num:
            print("Escolha um número maior!")
        else:
            print("Escolha um número menor!")

    jogadas += 1

print("---- Fim de jogo ----")
if jogadas <= 5:
    print("Você conseguiu rápido ein!")
elif jogadas <= 15:
    print("Éh... Até que não demorou tanto!")
else:
    print("Caramba... Que demora ein!")

print("O número era {}!".format(pc_num))
