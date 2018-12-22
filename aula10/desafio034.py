# imports

print("""
|*****************|
|    Desafio34    |
|*****************|
""")
print("Calculadora de Aumento Salarial")

sal = float(input("Digite o salário do funcionário: "))

if sal > 1250:
    percent = 0.10
else:
    percent = 0.15

new_sal = sal + (sal*percent)

print("""
Salário Antigo:       R$ {}
Salário Novo:         R$ {}
Porcentagem Recebida: {}%
""".format(sal, new_sal, percent*100))
