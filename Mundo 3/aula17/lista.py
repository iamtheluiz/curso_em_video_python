num = [0, 6, 3, 8, 5, 4]
# Adicionar novo item
num.append(8)
print(num)
# Adicionar novo item em um indice específico
num.insert(5, 12)
print(num)
# Retirar valor pelo indice
num.pop(0)
print(num)
# Ordenar lista
num.sort()
print(num)
# Cópia de Lista
a = [10, 20, 30, 40]
b = a    # Ligação
b = a[:] # Cópia
# Ordenar lista de maneira inversa
num.sort(reverse=True)
print(num)
# Remover um único elemento por seu valor
num.remove(8)
print(num)
# Verificar se existe um número na lista e remove-lo
if 4 in num:
    num.remove(4)
else:
    print("Não foi possível encontrar o número!")
# Pegar tamanho da lista
print(f'A lista tem {len(num)} itens')

print("")
print("="*10+"Lista Formatada"+"="*10)
lista = [10, 20, 60, 70, 49]
for i, valor in enumerate(lista):
    print(f'Na posição {i} é possível achar o valor {valor}!')
print('Acabei de verificar a lista!')

print("")
print("="*10+"Lista do Usuário"+"="*10)
lista = []
while True:
    lista.append(int(input("Digite um número inteiro: ")))

    continuar = ""
    while continuar != "S" and continuar != "N":
        continuar = input("Deseja continuar digitando? (S/N)").upper()

    if continuar == "N":
        break

for i, valor in enumerate(lista):
    print(f'Na posição {i} é possível achar o valor {valor}!')
print('Acabei de verificar a lista!')