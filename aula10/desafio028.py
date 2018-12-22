# imports
from random import randint

print("""
|*****************|
|    Desafio28    |
|*****************|
""")
print("Adivinhe o número")

pc_num = randint(0, 5)
u_num = int(input("Descubra qual número o computador escolheu! "))

print()
if pc_num == u_num:
    print("Você acertou! O número era {}!".format(pc_num))
else:
    print("Você errou! ;-; o número era {}...".format(pc_num))
