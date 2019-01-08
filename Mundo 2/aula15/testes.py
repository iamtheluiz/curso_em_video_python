soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    soma += num

print(f'A soma deu {soma}')
