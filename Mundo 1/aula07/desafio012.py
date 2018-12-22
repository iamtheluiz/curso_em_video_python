print("|*****************|")
print("|    Desafio12    |")
print("|*****************|")
print("")
print("Produto com 5% de desconto")
print();

preco = float(input("Digite o preço do produto: R$ "))

desconto = preco - ((preco/100)*5)

print()
print("O produto passou de R$ {} para R$ {}".format(preco, desconto))
