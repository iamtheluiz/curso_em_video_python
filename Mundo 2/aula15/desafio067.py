# imports

print("""
|******************|
|    Desafio067    |
|******************|
""")
print("Tabuada")
print()

while True:
    num = int(input("Digite um número: "))

    if num < 0:
        break
    else:
        c = 0
        print("======================")
        while c <= 10:
            print("{} x {} = {}".format(num, c, num * c))
            c += 1
        print("======================")
