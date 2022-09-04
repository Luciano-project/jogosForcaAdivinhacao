from random import randrange
class Adivinhacao:
    def __init__(self,idioma,chute=0):
        self.idioma=idioma
        self.pontos=1000
        self._total_de_tentativas=0
        self._numero_secreto=0
        self.chute=chute
        self._chutes=[]
        self.dificuldade_escolhida=''
        self.rodada=1
    
    def limpar_terminal(self):
        from os import system
        system('clear')
        
    def adiciona_historico_chutes(self):
        if self.chute!=0:
            self.historico_chutes.append(self.chute)
    
    @property
    def historico_chutes(self):
        return self._chutes
    
    def imprime_historico_chutes(self):
        print(f"{self.idioma.tentativas_anteriores}: ",end='')
        for chutes in self.historico_chutes:          
            print(chutes, end=', ')          
        print()
         
    def imprime_cabecalho(self):
        self.limpar_terminal()
        print("*********************************")
        print(f"{self.idioma.cabecalho}!")
        print("*********************************")

    def imprime_acertou(self):
        print(f"{self.idioma.imprime_acertou[0]} {self.pontos} {self.idioma.imprime_acertou[1]}!")
        
    def imprime_perdeu(self):
        print(f'{self.idioma.imprime_perdeu}{self.numero_secreto}')
    
    def imprime_chute_maior(self):
        print(f"{self.idioma.imprime_chute_maior}")        
        
    def imprime_chute_menor(self):
        print(f"{self.idioma.imprime_chute_menor}.")
    
    def imprime_numero_de_tentativas(self,rodada):
        print(f"\n{self.idioma.imprime_tentativas[0]} {rodada} {self.idioma.imprime_tentativas[1]} {self.total_de_tentativas}")  
    
    def imprime_fim_de_jogo(self):
        print(f"{self.idioma.imprime_fim_jogo}!")

    def define_numero_secreto(self):
        self._numero_secreto = randrange(1,101)
        
    @property
    def total_de_tentativas(self):
        return self._total_de_tentativas
    
    @total_de_tentativas.setter
    def total_de_tentativas(self,tentativas):
        self._total_de_tentativas=tentativas
    
    @property
    def numero_secreto(self):
        return self._numero_secreto
    
    def imprime_niveis_de_dificuldade(self):
        print(f"{self.idioma.imprime_nivel_dificuldade}")
     
    def dificuldade_do_jogo(self):
        self.imprime_niveis_de_dificuldade()
        nivel = int(input(": "))

        if(nivel == 1):
            self.total_de_tentativas = 20
            self.dificuldade_escolhida = self.idioma.dificuldade[0]
        elif(nivel == 2):
            self.total_de_tentativas = 10
            self.dificuldade_escolhida = self.idioma.dificuldade[1]
        else:
            self.total_de_tentativas = 5
            self.dificuldade_escolhida = self.idioma.dificuldade[2]
        
    def carrega_dados_do_jogo(self):
        self.imprime_cabecalho()
        self.dificuldade_do_jogo()        
    
    def digita_chute(self):
        chute_str = input(f"{self.idioma.digita_chute[0]}: ")
        print(f"{self.idioma.digita_chute[1]}" , chute_str)
        self.chute = int(chute_str)                
        #self.valida_intervalo(self.chute)
        
    def valida_intervalo_chute(self):
        chute = self.chute
        if(chute < 1 or chute > 100):
            print(f"{self.idioma.valida_intervalo}!")
            self.rodada-=1
            return True
        else:
            self.adiciona_historico_chutes()
             
    def atualiza_pontos(self):
        pontos_perdidos = abs(self.numero_secreto - self.chute)
        self.pontos = self.pontos - pontos_perdidos
        
    def valida_tentativa(self,rodada):
        acertou = self.chute == self.numero_secreto
        maior = self.chute > self.numero_secreto
        menor = self.chute < self.numero_secreto
        
        self.imprime_cabecalho() 
        if(acertou):
            self.imprime_acertou()
            return True
                   
        elif self.valida_intervalo_chute():
            return False
        
        else:
            if rodada>self.total_de_tentativas:
                self.imprime_perdeu()
                return False
             
            if(maior):
                self.imprime_chute_maior()

            elif(menor):
                self.imprime_chute_menor()
            self.atualiza_pontos()
            
    def carrega_info_jogando(self,rodada):
        self.imprime_historico_chutes()
        self.imprime_numero_de_tentativas(rodada)
    
    def jogando(self):
        self.define_numero_secreto()
        self.imprime_cabecalho()
        
        #for rodada in range(1, self.total_de_tentativas + 1, ):
        while self.rodada <= self.total_de_tentativas:
            self.carrega_info_jogando(self.rodada)
            self.digita_chute()
            self.rodada+=1
    
            if self.valida_tentativa(self.rodada):
                break
        
    def jogar(self):
        self.carrega_dados_do_jogo()
        resultado = self.jogando()      
        self.imprime_fim_de_jogo()

if(__name__ == "__main__"):
    Adivinhacao().jogar()
