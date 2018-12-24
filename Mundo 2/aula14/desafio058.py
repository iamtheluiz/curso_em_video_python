# imports
from random import randint

print("""
|******************|
|    Desafio058    |
|******************|
""")
print("Jogo da Adivinhação v2 (números de 0 a 10)")
print()

# Inicialização
tentativas = 0
acertou    = False

# PC escolhe um número
pc_num = randint(0, 10)

while not acertou:
    tentativas += 1
    u_num = int(input("Digite um número: "))

    if u_num == pc_num:
        acertou = True
    else:
        print("Tente novamente!")

print()
print("==== Fim do Jogo ====")
print("O número era {}!".format(pc_num))
print("Você precisou de {} tentativas para acertar".format(tentativas))
