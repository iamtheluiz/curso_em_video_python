print("|*****************|")
print("|    Desafio15    |")
print("|*****************|")
print("")
print("Aluguel de Carros")
print();

dias = float(input("Quantos dias o carro foi alugado? "))
kms = float(input("Quantos quilometros foram percorridos? "))

valor = (60*dias) + (kms*0.15)

print("O total a pagar é de R$ {:.2f}".format(valor));
