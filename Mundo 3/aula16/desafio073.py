# imports

print("""
|******************|
|    Desafio073    |
|******************|
""")
print("Tabela do Brasileirão!")

# Variáveis
tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

print("==== 5 Primeiros ====")
for pos, time in enumerate(tabela[:5]):
    print(f'{pos + 1}º => {time}')
print("==== 4 Últimos ====")
for pos in range(len(tabela) - 4, len(tabela)):
    print(f'{pos + 1}º => {tabela[pos]}')
print("==== Times em Ordem Alfabética ====")
for time in sorted(tabela):
    print(time)
print("==== Onde tá a Chapecoense?? ====")
print(f'Ela está em {tabela.index("Chapecoense") + 1}º lugar!')
