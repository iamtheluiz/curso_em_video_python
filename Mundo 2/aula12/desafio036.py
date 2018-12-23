# imports

print("""
|******************|
|    Desafio036    |
|******************|
""")
print("Aprovação de Empréstimo")

vl_casa = float(input("Qual é o valor da residência? "))
salario = float(input("Qual é o seu salário? "))
anos    = int(input("Em quantos anos você deseja quitar a casa? "))

# Transforma em meses
meses     = anos * 12
prestacao = vl_casa / meses # Valor de cada prestação mensal
porcento  = salario * 0.30 # 30% do salário

if porcento >= prestacao:
    # Empréstimo aprovado
    print("Seu empréstimo foi aprovado!")
    print("Valor total da Casa: {}".format(vl_casa))
    print("Seu Salário        : {}".format(salario))
    print("Anos para pagar    : {}".format(anos))
    print("Prestação Mensal   : {}".format(prestacao))
    print("30% do Salário     : {}".format(porcento))
else:
    print("Seu empréstimo não foi aprovado!")
    print("Valor total da Casa: {}".format(vl_casa))
    print("Seu Salário        : {}".format(salario))
    print("Anos para pagar    : {}".format(anos))
    print("Prestação Mensal   : {}".format(prestacao))
    print("30% do Salário     : {}".format(porcento))
