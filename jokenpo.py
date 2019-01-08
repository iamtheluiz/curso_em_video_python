# imports
from random import randint

print("JO-KEN-PÔ!")

while True:
    print("""
    ========== Qual você deseja jogar? ==========
                         _             _
                       _| |_         _| |
                      | | | |_      | | |
         _ _ _ _      | | | | |     | | |_ _      
       _| | | | |    _| | | | |    _| | | | |
      | | | | | |   | |       |   | | | | | |
      | |       |   | |       |   | |       |
       \________|    \________|    \________|
    
       1 - Pedra     2 - Papel    3 - Tesoura
    
    ========== Qual você deseja jogar? ==========    
    """)

    # Continua perguntando a escolha do jogador até ela ser válida
    escolha = False
    while not escolha:

        # Questiona o jogador
        escolha = int(input("Qual é sua escolha? "))
        escola = True

        # Verifica se a escolha é inválida
        if escolha != 1 and escolha != 2 and escolha != 3:
            escolha = False

    # Computador gera um número
    pc_escolha = randint(1, 3)

    # Verifica quem venceu
    if pc_escolha == 1 and escolha == 2:
        # Jogador ganha
        winner = "Jogador"
        loser = "PC"

    elif pc_escolha == 1 and escolha == 3:
        # PC ganha
        winner = "PC"
        loser = "Jogador"

    elif pc_escolha == 2 and escolha == 1:
        # PC ganha
        winner = "PC"
        loser = "Jogador"

    elif pc_escolha == 2 and escolha == 3:
        # Jogador ganha
        winner = "Jogador"
        loser = "PC"

    elif pc_escolha == 3 and escolha == 1:
        # Jogador ganha
        winner = "Jogador"
        loser = "PC"

    elif pc_escolha == 3 and escolha == 2:
        # PC ganha
        winner = "PC"
        loser = "Jogador"

    else:
        # Deu empate
        winner = "Empate"
        loser = "Empate"

    # Verifica a jogada de cada um
    if pc_escolha == 1:
        pc_jogou = "Pedra"
    elif pc_escolha == 2:
        pc_jogou = "Papel"
    else:
        pc_jogou = "Tesoura"

    if escolha == 1:
        jogador_jogou = "Pedra"
    elif escolha == 2:
        jogador_jogou = "Papel"
    else:
        jogador_jogou = "Tesoura"

    print("""
    ========== Resultado ==========
    Jogador:    {}
    Computador: {}
    """.format(jogador_jogou, pc_jogou))

    if winner != "Empate":
        print("O Vencedor é o {}!".format(winner.upper()))
    else:
        print("O jogo ficou EMPATADO!")

    print("=======================")
    fechar = ""
    while fechar != "N" and fechar != "S":
        fechar = input("Você deseja continuar jogando? (S ou N) ").upper()

    if fechar == "N":
        break

print("======================")
print("Jogo encerrado!")