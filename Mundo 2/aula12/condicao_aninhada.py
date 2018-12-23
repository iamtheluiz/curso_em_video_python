nome = str(input('Digite seu nome: '))

if nome in 'Júlio Rodolfo Diógenes Claúdio Ferraz Viviane Joelma Michelle Glicia':
    print("Seu nome me lembra um professor da minha escola...")
elif nome == "João" or nome == "Maria":
    print("Seu nome é muito popular no Brasil!")


print("Seja bem-vindo {}".format(nome))