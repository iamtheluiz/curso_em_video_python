# imports
from time import sleep

print("""
|******************|
|    Desafio099    |
|******************|
""")
print("Qual é o maior?!")
print()


# Funções
def maior(* nums):
    print("="*35)
    print("Verificando valores")
    maior = ""
    for num in nums:
        sleep(0.5)
        print(f'{num} ', end='', flush=True)
        if maior == "" or maior < num:
            maior = num

    print(f'foram verificados {len(nums)} valores')
    print(f"Na lista, o maior número é {maior}!")


# Programa Principal
maior(1, 20, 5, 60, 40, 5, 12, 9)
maior(7, 2, 30, 10, 50, 60, 90, 10, 5, 58, 8, 75)
maior(0)
