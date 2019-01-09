# imports

print("""
|******************|
|    Desafio076    |
|******************|
""")
print("Lista de Preços!")
print("")

# Variáveis
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'compasso', 9.99,
         'Mochila', 120.32)

print("="*45)
print(" "*15+"Lista de Preços".upper()+" "*15)
print("="*45)

for i, produto in enumerate(lista):
    if i % 2 == 0:
        # Nome do produto
        print(f'{produto:.<33}', end="")
    else:
        # Preço do produto
        print(f'R$ {produto:>9.2f}')
