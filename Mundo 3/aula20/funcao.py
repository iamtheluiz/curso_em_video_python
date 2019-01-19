def top(titulo):
    print('='*30)
    print(f'{titulo.upper():^30}')
    print('='*30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(* num):
    top("Contador")
    print(f'Foram passados {len(num)} números!')
    for n in num:
        print(f"  => {n}")

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa Principal
top('Olá querido Usuário!')
top('Relação de Candidatos!')
soma(4, 5)
contador(3, 2, 5)
top('Dobrador de Valor')
nums = [10, 3, 6, 2, 5]
dobra(nums)
print(nums)
