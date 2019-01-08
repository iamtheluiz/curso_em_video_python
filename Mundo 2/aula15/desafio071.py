# imports

print("""
|******************|
|    Desafio071    |
|******************|
""")
print("CAIXA IAMTHELUIZ!")

# Variáveis
saque        = ""
notas        = [50, 20, 10, 1]

# Pede para o usuário digitar o valor a ser sacado
while not saque.isnumeric():
    saque = input("Digite o valor que deseja sacar (número inteiro): R$ ")

# Converte o valor para inteiro
saque        = int(saque)

# Emite as notas
contador = 0
while saque != 0:
    nr_notas = saque // notas[contador]  # Quantidade de notas de tal valor
    saque -= nr_notas * notas[contador]  # Retira a soma das notas que saíram
    print(f'{nr_notas} cédulas de R$ {notas[contador]}')

    contador += 1

print("==========================")
print("Obrigado pela preferência!")
