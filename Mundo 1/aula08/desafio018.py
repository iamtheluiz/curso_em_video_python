# imports
from math import cos, sin, tan, radians

print("|*****************|")
print("|    Desafio18    |")
print("|*****************|")
print("")
print("Calculadora de Seno, Cosseno e Tangente")

angulo = float(input("Digite o valor de um ângulo: "))
rad = radians(angulo)

sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print()
print("O ângulo digitado foi {}º \nSeno: {} \nCosseno: {} \nTangente: {}".format(angulo, sen, cos, tan))
