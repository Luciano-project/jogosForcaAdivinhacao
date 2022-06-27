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
            print("Você errou, tente novamente!\nTentativas testantes {}".format(6-erros))
	
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print("\n{}".format(letras_acertadas))
    return acertou
     
def jogar():

    cabecalho()    
    print("Jogando forca")
    
    frutas = Arquivo().palavra()
    
    palavra_secreta=frutas[randrange(len(frutas))]
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)
    
    resultado=jogando(palavra_secreta,letras_acertadas)      
        
        	
    print("Fim do jogo")
    
    if resultado: print("você ganhou!")
    else: print("Você perdeu!\n\nA palavra era: {}".format(palavra_secreta))

if(__name__ == "__main__"):
    jogar()
