# imports

print("""
|******************|
|    Desafio044    |
|******************|
""")
print("Preço do produto com base no modo de pagar")

produto = float(input("Qual é o valor do produto? R$ "))
print("""
============= Formas de Pagamento =============
1 => À vista em Dinheiro (10% de desconto)
2 => À vista via Cheque (10% de desconto)
3 => À vista via Cartão (5% de desconto)
4 => 2 vezes via Cartão (Preço normal)
5 => 3 vezes ou mais via Cartão (20% de juros)
===============================================
""")
# Verifica o modo de pagamento
modo = 0
while modo == 0:
    # Só continua caso ele escolha um modo válido
    modo = int(input("Da tabela acima, escolha uma forma de pagamento: "))
    if modo != 1 and modo != 2 and modo != 3 and modo != 4 and modo != 5:
        modo = 0

if modo == 1 or modo == 2:
    # À vista Dinheiro ou Cheque
    if modo == 1:
        modo = "À vista em Dinheiro"
    else:
        modo = "À vista via Cheque"

    # Aplica 10% de desconto
    total = produto - (produto * 0.10)

elif modo == 3:
    # Á vista no Cartão
    modo = "À vista via Cartão"

    # Aplica 5% de desconto
    total = produto - (produto * 0.10)

elif modo == 4:
    # 2 vezes via Cartão
    modo = "2 vezes via Cartão"

    # Preço normal
    total = produto

elif modo == 5:
    # 3 vezes ou mais via Cartão
    modo = "3 vezes ou mais via Cartão"

    # 20% de Juros
    total = produto + (produto * 0.20)

else:
    # Erro
    modo  = "Padrão"
    total = "Padrão"

print()
print("======= Valores ========")
print("Produto:   R$ {}".format(produto))
print("Pagamento: {}".format(modo))
print("Total:     R$ {}".format(total))
