import adivinhacao
import forca

def escolha_jogo():
    print("*******************************")
    print("Escolha seu Jogo!")
    print("*******************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando adivinhalçao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()