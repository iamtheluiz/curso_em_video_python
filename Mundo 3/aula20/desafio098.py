# imports
from time import sleep

print("""
|******************|
|    Desafio098    |
|******************|
""")
print("Contador!")
print()


# Funções
def contador(inicio, fim, passo=1):
    print("="*35)
    print(f'Contagem de {inicio} até {fim} com passo {passo}')
    sleep(2)
    if passo == 0:
        passo = 1

    # Verifica se o inicio é maior que o fim
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    elif inicio < fim:
        fim += 1
        if passo < 0:
            passo *= -1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end="", flush=True)
        sleep(0.5)
    print("FIM!")


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

# Vez do usuário
print("===== Sua vez! =====")
ini = int(input("Início: "))
end = int(input("Fim   : "))
step = int(input("Passo : "))
contador(ini, end, step)
