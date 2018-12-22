# imports

print("""
|*****************|
|    Desafio30    |
|*****************|
""")
print("Impar ou Par?")

num = int(input("Digite um número inteiro! "))

print()
if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O número {} é impar".format(num))
