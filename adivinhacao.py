import random

def jogar():

    print("*******************************")
    print("Jogo de adivinhação!")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Define o nivel: "))


    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número emtre 1 e 100:"))
        print("Você digitou:", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar eum número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou {}!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! o chute foi maior que o número secreto")

            elif(menor):
                print("Você errou! seu chute foi menor que o numeor secreto")
                pontos_perdidos = abs(chute - numero_secreto)
                pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()