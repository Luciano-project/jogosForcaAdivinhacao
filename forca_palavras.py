import os
class Arquivo:
    def __init__(self):
        pass

    def adicionar(self,fruta):
        with open("palavras.txt", "a") as palavras:
            palavras.write("{}\n".format(fruta))
            print("Palavra adicionada com sucesso! ")
            return self.menu()

    def menu(self):
        print("*****Lista de palavras*****")
        print("(1) Adicionar (2) Listar palavras (0) Voltar")
        acao=int(input("Qual opcao? "))
        palavras = self.palavra()
        existe = False
        
        if acao == 1:
            fruta = input("Qual fruta adicionar? ").upper()
            for item in palavras: 
                if item==fruta:
                    existe = True
                    break
                    
            if existe:
                print("Já existe essa opcao!")
                return self.menu()
                
            elif not existe: return self.adicionar(fruta)
                
        elif acao == 2:
            self.listar_palavras()
            print()
            return self.menu()
            
        elif acao == 0:
            return 0
            
    def listar_palavras(self):
        os.system("clear")
        frutas = [item for item in self.palavra()]
        
        for item in frutas:
            print(item)
    	    
    def palavra(self):
        with open("palavras.txt", "r") as palavras:
            lista=palavras.read().upper()
            lista = lista.split() #como alternativa ao .split() podemos usar o . strip()
            return lista

if __name__ == "__main__":

    menu()
    
