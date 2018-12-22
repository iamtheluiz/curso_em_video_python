# imports

print("""
|*****************|
|    Desafio29    |
|*****************|
""")
print("Multa por velocidade (R$ 7 por km acima)")

km_hora = float(input("Digite a velocidade do carro: "))

if km_hora > 80:
    km_acima = km_hora - 80
    multa = float(7*km_acima)

    print("O carro está a {}km/h e acima da velocidade permitida!".format(km_hora))
    print("Multa aplicada: R$ {:.2f}".format(multa))
else:
    print("O carro está a {}km/h e dentro da velocidade permitida!".format(km_hora))
