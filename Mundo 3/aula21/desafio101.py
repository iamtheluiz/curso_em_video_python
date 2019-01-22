# imports

print("""
|******************|
|    Desafio101    |
|******************|
""")
print("Você Vota?!")
print()

# Variáveis


# Funções
def voto(nascimento):
    from datetime import date   # Função importada fica apenas dentro da função
    """
    -> Função que verifica se o usuário possuí idade para votar!
    :param nascimento: Ano de nascimento do Usuário
    :return: Retorna um texto com a referência de obrigatoriedade, ou não, do voto
    Luiz Gustavo da Silva Vasconcellos
    """
    ano_atual = date.today().year
    if nascimento > ano_atual:
        print("Você não pode usar um ano de nascimento maior que o ano atual!")
    else:
        idade = ano_atual - nascimento
        if idade < 16:
            return f"Com {idade}: NÃO VOTA!"
        elif idade < 18:
            return f"Com {idade}: VOTO OPCIONAL"
        elif idade < 65:
            return f"Com {idade}: VOTO OBRIGATÓRIO"
        else:
            return f"Com {idade}: VOTO OPCIONAL"


# Questiona nascimento do usuário
nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))
