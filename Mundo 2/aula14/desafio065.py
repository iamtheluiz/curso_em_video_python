# imports

print("""
|******************|
|    Desafio065    |
|******************|
""")
print("Média, Maior e Menor Valor!")
print()

rodando = True
soma    = 0
qt_nums = 0
maior   = 0
menor   = 0

while rodando:
    num = int(input("Digite um valor inteiro: "))

    soma    += num
    qt_nums += 1

    if maior == 0 or num > maior:
        maior = num

    if menor == 0 or num < menor:
        menor = num

    decisao = ""
    while decisao != "N" and decisao != "S":
        decisao = input("Você deseja continuar? (S ou N) ").upper()

    if decisao == "N":
        rodando = False

media = soma / qt_nums

print("O sistema computou {} números!".format(qt_nums))
print("A média entre todos resultou em {}".format(media))
print("O maior número digitado foi {}".format(maior))
print("E o menor número foi {}".format(menor))
