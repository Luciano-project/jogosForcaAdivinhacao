class IdiomaMenu:
    def __init__(self,idioma):
        self.idioma=idioma
        self.cabecalho="ESCOLHA SEU JOGO!"
        self.jogos="(1) Forca  (2) Adivinhação"
        self.qual_jogo="Qual jogo? (apenas números)"
        if self.idioma=="ingles":
            self.idioma_ingles()

    def idioma_ingles(self):
        self.cabecalho="CHOOSE YOUR GAME!"
        self.jogos="(1) Hangman  (2) Gessing Number"
        self.qual_jogo="Which game? (only numbers)"


class IdiomaForca:
    def __init__(self,idioma='portugues'):
        self.idioma=idioma
        self.escolha_tema='Escolha o tema'
        self.cabecalho='Bem vindo ao jogo da forca'
        self.qual_letra='Qual letra '
        self.fim_jogo='Fim de jogo'
        self.mensagem_enforcado='Puxa, voce foi enforcado'
        self.palavra_correta='A palavra era'
        self.mensagem_vencedor='Parabéns, você ganhou'
        self.escolha_tema='Escolha um tema'
        self.imprime_listas_palavras='(0) frutas (1) paises'
        self.imprime_historico_tentativas='Tentativas anteriores'

        if self.idioma=="ingles": self.idioma_ingles()

    def idioma_ingles(self):
        self.escolha_tema='Choose your theme'
        self.cabecalho='Welcome to hangman game'
        self.qual_letra='Which letter '
        self.fim_jogo='End game'
        self.mensagem_enforcado='Gosh, you were hanged'
        self.palavra_correta='The word was '
        self.mensagem_vencedor='Congratulations, you won'
        self.escolha_tema='choose theme'
        self.imprime_listas_palavras='(0) fruits (1) countries'
        self.imprime_historico_tentativas='Previous attemps'


class IdiomaAdivinhacao:
    def __init__(self,idioma):
        self.idioma=idioma
        self.cabecalho='Bem vindo ao jogo de Adivinhação'
        self.imprime_acertou='Você acertou e fez','pontos'
        self.imprime_perdeu='Poxa, você perdeu! O número secreto era: '
        self.imprime_chute_maior='Você errou! O seu chute foi maior do que o número secreto'
        self.imprime_chute_menor='Você errou! O seu chute foi menor do que o número secreto'
        self.imprime_tentativas='Tentativa','de'
        self.imprime_fim_jogo='Fim de jogo'
        self.imprime_nivel_dificuldade='Qual nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil'
        self.digita_chute='Digite um número entre 1 e 100','Você digitou'
        self.valida_intervalo='Você deve digitar um número entre 1 e 100'
        self.dificuldade=['Fácil','Médio','Difícil']
        self.tentativas_anteriores = 'Tentativas anteriores'
        if self.idioma=="ingles":
            self.idioma_ingles()

    def idioma_ingles(self):
        self.cabecalho='Welcome to guessing game'
        self.imprime_acertou='You got it right and did','points'
        self.imprime_perdeu='Gosh, you lose! The secret number was: '
        self.imprime_chute_maior='Your attempt was higher than the secret number'
        self.imprime_chute_menor='Your attempt was lower than the secret number'
        self.imprime_tentativas='Try', 'of'
        self.imprime_fim_jogo='End game'
        self.imprime_nivel_dificuldade='Which dificult level?\n(1) Easy  (2) Medium  (3) Hard'
        self.digita_chute='Write a number between 1 and 100','You writed'
        self.valida_intervalo='You must write a number between 1 and 100'
        self.dificuldade=['Easy','Medium','Hard']
        self.tentativas_anteriores = 'last attempts'
