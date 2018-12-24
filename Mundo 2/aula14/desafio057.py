# imports

print("""
|******************|
|    Desafio057    |
|******************|
""")
print("Válidador de Sexo")
print()

sexo = 0

while sexo == 0 or (sexo != "F" and sexo != "M"):
    sexo = input("Digite seu sexo (M ou F): ").upper()

if sexo == "M":
    sexo = "Masculino"
else:
    sexo = "Feminino"

print()
print("O sexo digitado foi {}".format(sexo))
