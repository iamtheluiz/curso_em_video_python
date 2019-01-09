# Isso é uma tupla (são imutáveis)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:])
print(lanche[:2])

print('==============')
for comida in lanche:
    print(comida)

print()
print('==============')
for pos, comida in enumerate(lanche):
    print(f'Eu irei comer {comida} na posição {pos+1}')

# Ordenação
print(sorted(lanche))

print()
print("============================")

# União de tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(f'Existe {c.count(5)} números 5 nessa tupla!')
print(f'O número 2 está na posição {c.index(2)}')
