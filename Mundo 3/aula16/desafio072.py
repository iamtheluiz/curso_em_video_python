# imports

print("""
|******************|
|    Desafio072    |
|******************|
""")
print("Números Por Extenso!")

# Variáveis
lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Recebe o número do usuário
while True:
    num = input("Digite um número entre 0 e 20: ")
    if num.isnumeric() and 21 > int(num) > -1:
        num = int(num)
        break

print('Você digitou o número {}'.format(lista[num]))
