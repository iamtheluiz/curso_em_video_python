# imports

print("""
|******************|
|    Desafio070    |
|******************|
""")
print("Preço e Produto!")

# Função que verifica se é um número
def isnum(num):
    try:
        float(num)
        return True
    except:
        pass
    return False
# Fim da Função

# Variáveis
contador  = 0
vl_total  = 0  # Valor da soma do preço de todos os produtos
mais_mil  = 0  # Quantidade de produtos que valem mais de mil reais
nm_barato = "" # Nome do produto mais barato
vl_barato = 0  # Valor do produto mais barato

while True:
    # Reseta os valores
    nome     = ""
    preco    = ""

    contador += 1
    while nome == "" or nome.isalnum() == False:
        nome  = input(f"Digite o nome do produto {contador}: ")
    while preco == "" or not isnum(preco):
        preco = input(f"Digit o valor do produto {contador}: R$ ")
    preco = float(preco)

    # Soma o valor no total
    vl_total += preco

    # Verifica se vale mais que mil reais
    if preco > 1000:
        mais_mil += 1

    # Verifica se é o produto mais barato
    if nm_barato == "" or preco < vl_barato:
        nm_barato = nome
        vl_barato = preco

    # Pergunta se o usuário deseja continuar digitando
    resposta = "";
    while resposta != "S" and resposta != "N":
        resposta = input("Você deseja continuar? (S/N) ").upper()

    if resposta == "N":
        break

print(f"""
======================================
- O total da compra foi R$ {vl_total}
- {mais_mil} produtos valem mais que R$ 1000
- O produto mais barato foi '{nm_barato}'!
    |- Preço: R$ {vl_barato}
""")
