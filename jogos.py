import forca
from forca_palavras import Arquivo
import adivinhacao
import idiomas_jogo as Idiomas


def printar_escolha_idioma():
    print("(1) Português  (2) English: ")

def define_idioma():
    printar_escolha_idioma()
    idioma=int(input(": "))
    lingua=''
    if idioma==1:
        lingua="portugues"
    elif idioma==2:
        lingua="ingles"

    idioma_menujogos=Idiomas.IdiomaMenu(lingua)
    idioma_forca=Idiomas.IdiomaForca(lingua)
    idioma_adivinhacao=Idiomas.IdiomaAdivinhacao(lingua)
    MenuJogos(idioma_menujogos,idioma_forca,idioma_adivinhacao,lingua).menu_jogo()

class MenuJogos:
    def __init__(self,menujogos,forca,adivinhacao,lingua):
        self._idioma_menujogos=menujogos
        self._idioma_forca=forca
        self._idioma_adivinhacao=adivinhacao
        self.lingua=lingua
# Tornamos o acesso indireto ao objeto dos idiomas
    @property
    def idioma_menu(self):
        return self._idioma_menujogos
    @property
    def idioma_forca(self):
        return self._idioma_forca
    @property
    def idioma_adivinhacao(self):
        return self._idioma_adivinhacao

    def limpar_terminal(self):
        from os import system
        system('clear')
        
    def cabecalho_inicio(self):
        self.limpar_terminal()
        print("*********************************")
        print(f'*******{self.idioma_menu.cabecalho}!*******')
        print("*********************************")

    def printa_escolhe_jogo(self):
        print(f"{self.idioma_menu.jogos}")

    def escolhe_jogo(self):
        self.cabecalho_inicio()
        self.printa_escolhe_jogo()
        jogo = int(input(f"{self.idioma_menu.qual_jogo}: "))
        return jogo
    
    def menu_jogo(self):
        jogo=self.escolhe_jogo()
        while True:
            if(jogo == 0):
                Arquivo().menu()
            
            elif(jogo == 1):
                forca.JogoForca(self.idioma_forca,self.lingua).jogar()
            elif(jogo == 2):
                adivinhacao.Adivinhacao(self.idioma_adivinhacao).jogar()

            else:
                print("INVÁLIDO!")
            break

if(__name__ == "__main__"):
   define_idioma()
