from random import randrange
from forca_palavras import Arquivo
import os
os.system("clear")

def cabecalho():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra 	
        index = index + 1
    

def jogando(palavra_secreta,letras_acertadas):
    enforcou,acertou=False,False
    erros=0
    
    while(not enforcou and not acertou):
        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(chute,palavra_secreta,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
	
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print("\n{}".format(letras_acertadas))
    return acertou


def jogar():

    cabecalho()
    
    lista_de_palavras = Arquivo().palavra()
 
    palavra_secreta=lista_de_palavras[randrange(len(lista_de_palavras))]
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)
    
    resultado=jogando(palavra_secreta,letras_acertadas)      
            	
    print("Fim do jogo")
    
    if resultado:
        imprime_mensagem_vencedor()
        
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_perdedor(palavra_secreta):

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
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))

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
