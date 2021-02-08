from Tela import Tela
from Celula import Celula

from tkinter import *

class Jogo(Tela):
    def __init__(self, resolucao):
        # Inicia o objeto Tela
        Tela.__init__(self, resolucao)
        
        # Define um comando pro botão do objeto Tela
        self.butjogo['command'] = self.IniciaSimulação
        self.butjogo['bg'] = 'red'

        # Variável que determina o funcionamento 
        self.edicao = True
        self.atualizacao = 100

        # Armazena a copia das instancias
        self.copia = []

        # -- Os bingings -- 

        # Botão esquerdo do mouse (LMB)
        self.canvas.bind('<Button-1>', self.BotaoEsquerdo)
        self.canvas.bind('<B1-Motion>', self.BotaoEsquerdo)
        # Botão direito do mouse (RMB)
        self.canvas.bind('<Button-3>', self.BotaoDireito)
        self.canvas.bind('<B3-Motion>', self.BotaoDireito)

        # Inicia a Updatar a Tela
        self.Update()

        # Essa instancia usada vem do objeto Tela
        self.canvas.focus_force()
        self.inst.mainloop()
    
    # O que diferencia o comando do RMB do comando do LMB
    def BotaoEsquerdo(self, event):
        self.OnClick(ative=True, event=event)
    def BotaoDireito(self, event):
        self.OnClick(ative=False, event=event)

    def OnClick(self, ative, event):
        # -- Quando Clicar -- 
        coord = (event.x, event.y)
        elemento = self.canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1])

        if len(elemento) >= 1:
            if (elemento[0] in self.copia) or len(self.copia) == 0:
                self.copia.append(elemento[0])
                '''for i in range(len(self.Celulas)):
                    if self.Celulas[i].celula == elemento[0]:
                        self.Celulas[i].Gerencia(ative)
                        break'''

                for setor in self.Celulas:
                    for celulas in setor:
                        if celulas.celula == elemento[0]:
                            celulas.Gerencia(ative)
                            break
 
    def Update(self):
        # -- Faz as atualizações na tela --
        atualiza = 10

        for elemento in self.copia: # Pega os elementos colocados para atualizar e os atualiza
            for setor in self.Celulas:
                for celulas in setor:
                    if celulas.celula == elemento:
                        if celulas.state:
                            celulas.Ativa()
                        else:
                            celulas.Desativa()
                        
                        self.copia.remove(elemento)
                        break
                            
        if self.edicao == False:
            atualiza = self.atualizacao
            self.ChecaVida()

        self.inst.after(atualiza, self.Update)


    def IniciaSimulação(self):
        # -- Prepara para inicializar a simulação --
        self.MudaCor('yellow') 

        self.edicao = False

        self.butjogo['bg'] = 'lime'
        self.butjogo['text'] = 'PARAR'
        self.butjogo['command'] = self.ParaSimulacao


    def ParaSimulacao(self):
        self.MudaCor('white')

        self.edicao = True

        self.butjogo['bg'] = 'red'
        self.butjogo['text'] = 'INICIAR'
        self.butjogo['command'] = self.IniciaSimulação

    def MudaCor(self, cor):
        for setor in self.Celulas:
            for celula in setor:
                celula.ativada = cor

                if celula.state == True:
                    celula.Ativa()

    def ChecaVida(self):
        for i_setor in range(len(self.Celulas)):
            setor = self.Celulas[i_setor]
            for i_celulas in range(len(setor)):
                celula = setor[i_celulas]
                
                vivas = 0
                for y in range(-1, 2): # Coloquei 2 pq o range diminui 1 valor
                    for x in range(-1, 2):
                        try:
                            if self.Celulas[i_setor+y][i_celulas+x].state == True and (x, y) != (0, 0):
                                vivas += 1 
                        except: pass
                
                if (vivas < 2 or vivas > 3) and celula.state == True:
                    celula.Gerencia(False)
                    self.copia.append(celula.celula)

                if vivas == 3 and celula.state == False:
                    celula.Gerencia(True)
                    self.copia.append(celula.celula)


# Inicia o game
resolucao = '1020x760'
Jogo(resolucao)