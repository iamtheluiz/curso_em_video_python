print("\033[31m|***************************|")
print("|      Arvore de Natal      |")
print("|  Obs: Tamanho precisa ser |")
print("| maior que 2               |")
print("|***************************|")
tamanho = 1

while tamanho < 3:
    tamanho = int(input("Qual a altura da sua arvore? \033[m"))

print("\033[32m")
contador = 0
tamanho_final = (tamanho*2) - 1

# Faz o corpo
while contador < tamanho:
    print(" "*int(((tamanho_final - 1) / 2) - contador), "*"*((contador*2)+1))
    contador += 1

# Coloca o tronco
print("\033[m "*int(((tamanho_final - 1) / 2)), "|")
print(" ", "-"*(tamanho_final-2))
