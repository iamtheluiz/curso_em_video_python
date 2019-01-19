pessoa = {'nome': 'Luiz', 'sexo': 'M', 'idade': 17}
print(pessoa['nome'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos!')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print("-="*25)
for key in pessoa.keys():
    print(key)

print("-="*25)
for value in pessoa.values():
    print(value)

print("-="*25)
del pessoa['sexo']
pessoa['nome'] = "Eduardo"
pessoa['peso'] = 98.5
for key, value in pessoa.items():
    print(f'{key.title()} = {value}')

print("-="*25)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print("-="*25)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
print(brasil)
for estado in brasil:
    for key, val in estado.items():
        print(f'O campo {key} tem valor {val}')
