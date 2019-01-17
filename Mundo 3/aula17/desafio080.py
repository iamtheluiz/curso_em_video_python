# imports

print("""
|******************|
|    Desafio080    |
|******************|
""")
print("Ordenação sem Sort (5 valores)")
print()

# Variáveis
numeros = []

# Input do usuário
for i in range(0, 5):
    num = int(input("Digite um valor inteiro: "))

    # Percorre a lista e vê sua posição
    if i == 0:
        numeros.append(num)
        print("Adicionado como primeiro valor...")
    else:
        colocado = False
        for numero in numeros:
            if num < numero and not colocado:
                print(f"Adicionado na posição {numeros.index(numero)}...")
                numeros.insert(numeros.index(numero), num)
                colocado = True
        if not colocado:
            numeros.append(num)
            print("Adicionado ao final da lista...")

print("-="*20)
print(f'Os valores digitados, em ordem, foram: {numeros}')
