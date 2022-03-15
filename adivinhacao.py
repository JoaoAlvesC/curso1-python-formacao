import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("1-facil 2-medio 3-dificil")
    dificuldade = int(input("Escolha o nível: "))

    if(dificuldade == 1):
        tentativas = 10
    elif(dificuldade ==  2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1,tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        number = input("Digite o número entre 1 e 100: ")

        number_int = int(number)

        if number_int < 1 or number_int > 100:
            print("Warning: Você deve digitar um número entre 1 e 100")
            continue

        acertou = number_int == secret_number
        menor = number_int < secret_number
        maior = number_int > secret_number

        if (acertou):
            print("Acertou!!! Pontuação: {}".format(pontos))
            break
        else:
            if (menor):
                print("Você digitou um número menor que o número correto")
            elif (maior):
                print("Você digitou um número maior que o número correto")
            pontos_perdidos = abs(secret_number - number_int)
            pontos -= pontos_perdidos

    print("Fim do jogo! O número correto era {}".format(secret_number))



