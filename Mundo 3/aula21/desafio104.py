# imports

print("""
|******************|
|    Desafio104    |
|******************|
""")
print("Validação do Input (Apenas números inteiros)")
print()


# Funções
def leiaInt(mensagem):
    """
    -> Função que aceita somente valores de 'input' do tipo inteiro
    :param mensagem: Mensagem exibida ao pedir para o usuário digitar um número
    :return: Retorna o número digitado pelo usuário
    """
    num = ''
    while not num.isnumeric():
        num = input(mensagem)

        if not num.isnumeric():
            print("\033[31mERRO! Digite um número inteiro!\033[m")

    return num


num = leiaInt("Digite um número inteiro: ")
print(f'Você digitou o número {num}')
