# imports

print("""
|******************|
|    Desafio058    |
|******************|
""")
print("Dois valores, um menu")
print()

# Variáveis de Inicialização
executar = True     # Guarda se o programa deve continuar executando
trocar   = False    # Verifica se o usuário deseja trocar os números
n1 = n2 = 0

while executar:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor : "))
    trocar = False

    # Enquanto o usuário não quiser trocar os números
    while not trocar:
        print("=== O que você deseja realizar? ===")
        print("[1] Soma")
        print("[2] Multiplicação")
        print("[3] Qual é maior?")
        print("[4] Digitar novos números")
        print("[5] Sair do Programa")
        opcao = int(input("Digite sua opção: "))

        if opcao == 1:
            # Soma dos números
            print("A soma entre {} e {} resulta em {}".format(n1, n2, n1+n2))
            print()

        elif opcao == 2:
            # Multiplicação dos números
            print("{} multiplicado por {} resulta em {}".format(n1, n2, n1*n2))
            print()

        elif opcao == 3:
            # Qual é maior?
            if n1 > n2:
                print("O número {} é maior que {}!".format(n1, n2))
            elif n2 > n1:
                print("O número {} é maior que {}!".format(n2, n1))
            else:
                print("Os números {} e {} são iguais!".format(n1, n2))
            print()

        elif opcao == 4:
            trocar = True

        elif opcao == 5:
            trocar = True
            executar = False

print("Encerrado!")