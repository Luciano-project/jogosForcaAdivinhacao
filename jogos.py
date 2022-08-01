import forca
from forca_palavras import Arquivo
import adivinhacao


def cabecalho_inicio():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

def printa_escolhe_jogo():
    print("(1) Forca (2) Adivinhação")

def escolhe_jogo():
    cabecalho_inicio()
    printa_escolhe_jogo()
    jogo = int(input("Qual jogo? "))
    return jogo
    
def menu_jogo():
    jogo=escolhe_jogo()
    while True:
        if(jogo == 0):
            Arquivo().menu()
            
        elif(jogo == 1):
            JogoForca.jogar()
   
        elif(jogo == 2):
            adivinhacao.jogar()

        else:
            print("Digite uma opção válida!")

        break        

if(__name__ == "__main__"):
    menu_jogo()
