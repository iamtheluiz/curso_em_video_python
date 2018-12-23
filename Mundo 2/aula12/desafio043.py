# imports

print("""
|******************|
|    Desafio043    |
|******************|
""")
print("Calculo de IMC")

peso   = float(input("Quanto você pesa (kg)? "))
altura = float(input("Quanto você mede  (m)? "))

imc = peso / altura**2

print()
if imc < 18.5:
    condicao = "Abaixo do Peso"
elif imc < 25:
    condicao = "Peso Ideal"
elif imc < 30:
    condicao = "Sobrepeso"
elif imc < 40:
    condicao = "Obesidade"
elif imc >= 40:
    condicao = "Obesidade Mórbida"
else:
    condicao = "Padrão"
    print("Ocorreu um erro ao definir seu IMC!")

print("===== Resultados =====")
print("Peso:     {} kg".format(peso))
print("Altura:   {} m".format(altura))
print("IMC:      {} ".format(imc))
print("Condição: {} ".format(condicao))
