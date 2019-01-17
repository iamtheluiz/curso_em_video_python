# imports

print("""
|******************|
|    Desafio078    |
|******************|
""")
print("Lista de Números")
print("")

# Variáveis
nums = []
maior = ""
menor = ""
index_maior = []
index_menor = []


# Função que formata o texto
def formatar_texto(lista):
    count = 0
    if len(lista) == 1:
        texto = "na posição"
    else:
        texto = "nas posições"
    while count < len(lista):
        if len(lista) == 1:
            texto += f" {count + 1}"
        elif count == 0 and count < len(lista) - 1:
            texto += f" {count + 1}"
        elif count < len(lista) - 1:
            texto += f", {count + 1}"
        else:
            texto += f" e {count + 1}"
        count += 1

    return texto


# Pega os 5 números
for i in range(0, 5):
    nums.append(int(input(f"Digite o {i+1}º número inteiro: ")))

    # Verifica o número
    if maior == "" or maior < nums[i]:
        maior = nums[i]
        index_maior = [i]
    elif nums[i] == maior:
        index_maior.append(i)

    if menor == "" or menor > nums[i]:
        menor = nums[i]
        index_menor = [i]
    elif nums[i] == menor:
        index_menor.append(i)

texto_maior = formatar_texto(index_maior)
texto_menor = formatar_texto(index_menor)

# Exibe o resultado do programa
print("="*20)
print(f"O maior número digitado foi {maior} {texto_maior}")
print(f"O maior número digitado foi {menor} {texto_menor}")

