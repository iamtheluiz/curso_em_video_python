# imports

print("""
|******************|
|    Desafio040    |
|******************|
""")
print("Aprovado, Recuperação ou Reprovado?")

n1    = float(input("Digite sua primeira nota: "))
n2    = float(input("Digite sua segunda nota : "))
media = (n1 + n2) / 2

print()
if media < 5:
    print("\033[31mPoxa... Você foi reprovado... Mas continue estudando! :)\033[m")
elif media < 7:
    print("\033[34mVocê vai precisar fazer recuperação!\033[m")
elif media >= 7:
    print("\033[32mParabéns! Você foi aprovado!\033[m")

print("Média Final: {}".format(media))
