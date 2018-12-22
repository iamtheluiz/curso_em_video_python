# Imports
from math import floor

print("|*****************|")
print("|    Desafio16    |")
print("|*****************|")
print("")
print('Parte inteira de um número')

num = float(input("Digite um número real: "))

p_int = floor(num)

print()
print('O número {} tem parte inteira {}'.format(num, p_int))
