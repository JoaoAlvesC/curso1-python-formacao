import forca
import adivinhacao 

print("*********************************")
print("Escolha o jogo!")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()