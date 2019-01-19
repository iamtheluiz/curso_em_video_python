# imports

print("""
|******************|
|    Desafio096    |
|******************|
""")
print("Área do Terreno Retângular")
print()

# Funções
def area(l, c):
    a = l*c
    print(f'A área do terreno de {l}m x {c}m é de {a} m²')

# Variáveis
largura = float(input("Largura do terreno (m): "))
comprimento = float(input("Comprimento do terreno (m): "))
area(largura, comprimento)
