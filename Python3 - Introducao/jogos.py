import forca
import adivinhacao

print("*********************************")
print("********Escolha seu jogo!********")
print("********************************* \n")
print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando forca: \n")
    forca.jogar()
else:
    print("Jogando adivinhação: \n")
    adivinhacao.jogar()
