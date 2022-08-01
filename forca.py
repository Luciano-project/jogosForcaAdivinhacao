from random import randrange
from forca_palavras import Arquivo, PalavraJogo
import os
os.system("clear")

class JogoForca:
    def __init__(self,palavra='',lista=[],letras_acertadas=''):
        self._palavra_secreta=palavra
        self._lista_de_palavras=lista
        self._letras_acertadas=letras_acertadas
        self.acertou=False
        self.enforcou=False
        
    @property
    def letras_acertadas(self):
        return self._letras_acertadas
        
    @property
    def palavra_secreta(self):
        return self._palavra_secreta
        
    @property
    def lista_de_palavras(self):
        return self._lista_de_palavras
    
    def define_letras_acertadas(self):
        self._letras_acertadas = ["_" for letra in self.palavra_secreta]
    
    def importa_lista_de_palavras(self):
        self._lista_de_palavras=PalavraJogo().retorna_a_lista()

    def define_palavra_secreta(self):
        self._palavra_secreta=self.lista_de_palavras[randrange(len(self.lista_de_palavras))]

    def carrega_dados_do_jogo(self):
        self.importa_lista_de_palavras()
        self.define_palavra_secreta()
        self.define_letras_acertadas()
        JogoForca.cabecalho()
        
    @staticmethod
    def cabecalho():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***") 
        print("*********************************")

    def pede_chute(self):
        chute = input("\n\nQual letra? ")
        chute = chute.strip().upper()
        return chute

    def marca_chute_correto(self,chute):
        index = 0
        for letra in self.palavra_secreta:
            if(chute == letra):
                self.letras_acertadas[index] = letra 	
            index = index + 1
            
    def verifica_resultado_do_jogo(self,erros):
        self.enforcou = erros == 7
        self.acertou = "_" not in self.letras_acertadas        
        
    
    def imprime_letras_acertadas(self):
        #print(self.letras_acertadas)
        for letra in self.letras_acertadas:
            print(f"'{letra}' ",end='')    
        
    def jogando(self):
        erros=0
        while(not self.enforcou and not self.acertou):
            chute = self.pede_chute()
            erros+=self.resultado_do_chute(erros,chute)       
            self.verifica_resultado_do_jogo(erros)
            self.imprime_letras_acertadas()
        return self.acertou

    def resultado_do_chute(self,erros,chute):
        if chute in self.palavra_secreta:
            self.marca_chute_correto(chute)
            return 0
        
        else:
            erros+=1
            JogoForca.desenha_forca(erros)
            return 1

    def jogar(self):
        self.carrega_dados_do_jogo()
        self.imprime_letras_acertadas()
        resultado=self.jogando()      
        self.fim_de_jogo(resultado)
    
    def fim_de_jogo(self,resultado):
        print("\nFim do jogo!")
        if resultado:
            JogoForca.imprime_mensagem_vencedor()
        
        else:
            JogoForca.imprime_mensagem_perdedor(self.palavra_secreta)
            
    @staticmethod
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
        
    @staticmethod
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
        
    @staticmethod
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
    JogoForca().jogar()
