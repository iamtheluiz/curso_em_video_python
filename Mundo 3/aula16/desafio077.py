# imports

print("""
|******************|
|    Desafio077    |
|******************|
""")
print("Vogais nas Palavras")
print("")

# Variáveis
palavras = ('Aprender', 'Programar', 'Jogar', 'Desafios', 'Interesse', 'Pertinencia', 'Achocolatado', 'Biscoito', 'Linguagem', 'Cobol')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f"Na palavra {palavra.upper()} temos as vogais: ", end="")
    lista_vogais    = ""
    lista_formatada = ""

    # Verifica as vogais
    for vogal in vogais:
        if palavra.count(vogal) > 0:
            lista_vogais += vogal.upper()

    # Formata a exibição das vogais
    if len(lista_vogais) == 0:
        lista_formatada = "Não existe nenhuma vogal!"
    elif len(lista_vogais) == 1:
        lista_formatada = lista_vogais
    elif len(lista_vogais) >= 2:
        for i in range(0, len(lista_vogais)):
            if i == 0:
                lista_formatada = ""
            elif i == len(lista_vogais) - 1:
                lista_formatada += " e "
            else:
                lista_formatada += ", "
            lista_formatada += lista_vogais[i]

    print(lista_formatada)
