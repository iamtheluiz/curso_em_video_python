# imports

print("""
|******************|
|    Desafio049    |
|******************|
""")
print("Tabuada com FOR")

num = int(input("Digite um número inteiro: "))

for i in range(0, 11):
    print("{} x {} = {}".format(num, i, num * i))
