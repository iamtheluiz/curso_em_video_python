print("|*****************|")
print("|    Desafio13    |")
print("|*****************|")
print("")
print("Salário com 15% de aumento")
print();

salario = float(input("Digite o salário do funcionário: R$ "))

aumento = salario + ((salario/100)*15)

print("O salário do funcionário aumentou de R$ {} para R$ {}".format(salario, aumento))
