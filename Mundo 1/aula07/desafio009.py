print("|*****************|")
print("|    Desafio09    |")
print("|*****************|")
print("")
print("Tabuada")

num = int(input("Digite um número inteiro: "))

count = 0
while count <= 10:
    print("{} x {} = {}".format(num, count, num*count))
    count += 1
