import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("(Chute deve estar entre 1 e 100!) \n")

    #numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 200
    ganhou = False

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {0} de {1} \n".format(rodada, total_de_tentativas))
        #"R$ {:07.2f}".format(4.5)
        #"Data {:02d}/{:02d}".format(9,4)

        chute = input("Digite o seu numero: ")
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if(numero_secreto == int(chute)):
            ganhou = True
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            else:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if(ganhou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(numero_secreto)

    print("Pontos: {:03d}".format(pontos))


def imprime_mensagem_perdedor(numero_secreto):
    print("Puxa, você foi perdeu!")
    print("O número era {}".format(numero_secreto))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if(__name__ == "__main__"):
    jogar()
