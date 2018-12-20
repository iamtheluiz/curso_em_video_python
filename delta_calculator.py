import math

print("|**********************|")
print("|         Delta        |")
print("|       Calculador     |")
print("|**********************|")
a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

delta = (b*b)-(4*a*c)
sqrt_delta = math.sqrt(delta)
x1 = ((-b) + sqrt_delta)/(2*a)
x2 = ((-b) - sqrt_delta)/(2*a)

print("")
print("")
print("|**********************|")
print("|      Resultados      |")
print("|**********************|")
print("Delta:",delta)
print("X1:",x1)
print("X2:",x2)
