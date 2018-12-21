# imports
from math import sqrt

print("|*****************|")
print("|    Desafio17    |")
print("|*****************|")
print("")
print("Calculadora de Hipotenusa")

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hip = sqrt((co**2) + (ca**2))

print("A hipotenusa vale {}".format(hip))
