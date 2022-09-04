import idiomas_jogo as Idioma

class PalavraJogo:
    def __init__(self,idioma_objeto=Idioma.IdiomaForca("portugues"),idioma='portugues'):
        self.idioma_objeto=idioma_objeto
        self.idioma=idioma
        self.palavra_sorteada=''
        self.path=Arquivo().path
     
    def retorna_a_lista(self):
        print(f"\n{self.idioma_objeto.escolha_tema}:")
        self.imprime_listas_palavras()
        destino=int(input())

        self.path+=Arquivo(self.idioma).lista_de_arquivos[destino]

        with open(self.path, "r") as palavras:
            lista=palavras.read().upper()
            lista_de_palavras = lista.split()
            return lista_de_palavras

    def imprime_listas_palavras(self):
#        print(self.idioma)
        print(f'{self.idioma_objeto.imprime_listas_palavras}')

class Arquivo:
    def __init__(self,idioma='portugues',listas=['frutas.txt','paises.txt']):
        self.idioma=idioma
        self.lista_de_palavras=[]
        self._lista_de_arquivos=listas
        self.path="palavras/"
        self.path_padrao="palavras/"
        self._palavra_secreta=''
        self.lista_selecionada=''
        if self.idioma=='ingles':
            self.muda_arquivos_para_ingles()
    @property
    def lista_de_arquivos(self):
        return self._lista_de_arquivos

# mudança de idioma
    def muda_arquivos_para_ingles(self):
        self._lista_de_arquivos = ['frutas-en.txt','paises-en.txt']
        self.idioma="ingles"

    def imprime_cabecalho_menu(self):
        print("\n\n*****Lista de palavras da forca*****")

    def imprime_opcoes_menu(self):
        print("(1) Adicionar (2) Listar palavras (0) Sair")

    def imprime_idioma_selecionado(self):
        print(f"\nidioma selecionado: {self.idioma.title()}\n")

    def imprime_listar_palavras_bordas(self,ordem):
        forma="-"*20+f"{self.lista_selecionada}"+"-"*20
        if ordem==1:
            print(forma)
        elif ordem==2:
            print(f"-"*len(forma)+"\n")
        


    def adiciona_palavra_forca(self,palavra_a_ser_adicionada):
        with open(self.path, "a") as palavras:
            palavras.write("{}\n".format(palavra_a_ser_adicionada))
            print("Palavra adicionada com sucesso! ")

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


    def escolhe_idioma(self):
        print("(1) Arquivos em inglês  (2) Arquivos em português")
#self.imprime_idioma_arquivos()
        escolha=int(input(": "))
        if escolha==1:
            self.muda_arquivos_para_ingles()

    def escolhe_lista_palavras(self):
        caminho=input("selecione a lista: ")
        self.path+=self.lista_de_arquivos[int(caminho)]
        self.lista_selecionada=self.lista_de_arquivos[int(caminho)]

    def carrega_dados(self):
        self.imprime_cabecalho_menu()
        PalavraJogo(Idioma.IdiomaForca(self.idioma),self.idioma).imprime_listas_palavras()
        self.escolhe_lista_palavras()
        self.imprime_cabecalho_menu()


    def menu(self):
        self.escolhe_idioma()
        self.carrega_dados()
        palavras = self.palavra()
        while True:
            self.imprime_opcoes_menu()
            self.imprime_idioma_selecionado()
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
        self.imprime_listar_palavras_bordas(1)
        for item in self.lista_de_palavras:
            print(item)
        self.imprime_listar_palavras_bordas(2)
    	    
    def palavra(self):
        with open(self.path, "r") as palavras:
            lista=palavras.read().upper()
            self.lista_de_palavras = lista.split() #como alternativa ao .split() podemos usar o . strip()
            return lista
            

if __name__ == "__main__":
    Arquivo().menu()
