import forca
from forca_palavras import Arquivo
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))
    while True:
        if(jogo == 0):
            print("Adicionar palavras a forca")
            if Arquivo().menu()==0: return escolhe_jogo()
            
        elif(jogo == 1):
            print("Jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        acao=input("\n\nJogar novamente? (s/n)\n")
        if acao=="s":
            return escolhe_jogo()
        else: break
if(__name__ == "__main__"):
    escolhe_jogo()
