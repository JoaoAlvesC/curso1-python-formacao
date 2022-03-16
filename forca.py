import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Forca! *****")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not acertou and not enforcou):
        chute = input("Chute uma letra: ").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
            
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        
    if (acertou) :
        print("YOU WON")
    else:
        print("YOU LOSE")

    print("Fim do jogo")




