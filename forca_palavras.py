import os

class PalavraJogo:
    def __init__(self):
        self.palavra_sorteada=''
        self.path=Arquivo().path
     
    def retorna_a_lista(self):
        print("\nEscolha um tema:")
        Arquivo().imprime_listas_palavras()
        destino=int(input())
        self.path+=Arquivo().lista_de_arquivos[destino]
        
        with open(self.path, "r") as palavras:
            lista=palavras.read().upper()
            lista_de_palavras = lista.split() #como alternativa ao .split() podemos usar o . strip()
            return lista_de_palavras
         
    
class Arquivo:
    def __init__(self):
        self.lista_de_palavras=[]
        self.lista_de_arquivos=['frutas.txt','paises.txt']
        self.path="palavras/"
        self.path_padrao="palavras/"
        self._palavra_secreta=''
    
    def adiciona_palavra_forca(self,palavra_a_ser_adicionada):
        with open(self.path, "a") as palavras:
            palavras.write("{}\n".format(palavra_a_ser_adicionada))
            print("Palavra adicionada com sucesso! ")
    
    #def adiciona_listas_forca(self): 
    #    for c in os.listdir(self.path_padrao):
    #        self.lista_de_arquivos.append(c)
        
    def imprime_cabecalho_menu(self):
        self.limpa_terminal()
        print("*****Lista de palavras da forca*****")
        
    def imprime_opcoes_menu(self):    
        print("(1) Adicionar (2) Listar palavras (0) Voltar")
                      
    def verifica_palavra_existente(self,palavra_para_adicionar):
        existe=False
        for item in self.lista_de_palavras: 
            if item==palavra_para_adicionar:
                existe = True
                break
                   
        if existe:
            print("Já existe essa opcao!")
               
        elif not existe:
            self.adiciona_palavra_forca(palavra_para_adicionar)
              
    def imprime_listas_palavras(self):
        print('(0) frutas (1) paises')
            
            
    def escolhe_lista_palavras(self):
        caminho=input("selecione a lista: ")
        self.path+=self.lista_de_arquivos[int(caminho)]
        
    def carrega_dados(self):
        self.imprime_listas_palavras()
     #   self.adiciona_listas_forca()
        self.escolhe_lista_palavras()
        
        
        
    def menu(self):
        self.imprime_cabecalho_menu()
        self.carrega_dados()
        self.imprime_cabecalho_menu()
        palavras = self.palavra()        
        while True:
            self.imprime_opcoes_menu()
            acao=int(input("Qual opcao? "))
            if acao == 1:
                palavra_para_adicionar = input("Qual item adicionar? ").upper()
                self.verifica_palavra_existente(palavra_para_adicionar)
                
            elif acao == 2:
                self.imprime_cabecalho_menu()
                self.listar_palavras()
            
            elif acao == 0:
                return 

    def limpa_terminal(self):
        os.system("clear")
        
    def listar_palavras(self):
        for item in self.lista_de_palavras:
            print(item)
    	    
    def palavra(self):
        with open(self.path, "r") as palavras:
            lista=palavras.read().upper()
            self.lista_de_palavras = lista.split() #como alternativa ao .split() podemos usar o . strip()
            return lista
            

if __name__ == "__main__":
    Arquivo().menu()
