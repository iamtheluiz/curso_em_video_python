# imports

print("""
|******************|
|    Desafio097    |
|******************|
""")
print("Texto que acompanha o tamanho da String")
print()


# Funções
def escreva(texto, espaco=2):
    espaco = espaco * 2
    tamanho = len(texto) + espaco
    print('~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('~'*tamanho)


# Programa Principal
escreva("Luiz Gustavo", 4)
escreva("Teste?", 1)
escreva("Curso em Vídeo de Python")
