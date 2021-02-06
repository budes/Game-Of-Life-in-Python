from Tela import Tela
from Celula import Celula

from tkinter import *

class Jogo(Tela):
    def __init__(self, resolucao):
        # Inicia o objeto Tela
        Tela.__init__(self, resolucao)
        
        # Armazena a copia das instancias
        self.copia = []

        # -- Os bingings -- 

        # Botão esquerdo do mouse (LMB)
        self.inst.bind('<Button-1>', self.BotaoEsquerdo)
        self.inst.bind('<B1-Motion>', self.BotaoEsquerdo)
        # Botão direito do mouse (RMB)
        self.inst.bind('<Button-3>', self.BotaoDireito)
        self.inst.bind('<B3-Motion>', self.BotaoDireito)

        # Inicia a Updatar a Tela
        self.Update()

        # Essa instancia usada vem do objeto Tela
        self.inst.focus_force()
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

        #print(coord)

        print(ative)
        if len(elemento) >= 1:
            if (elemento[0] in self.copia) or len(self.copia) == 0:
                self.copia.append(elemento[0])
                for i in range(len(self.Celulas)):
                    if self.Celulas[i].celula == elemento[0]:
                        self.Celulas[i].Gerencia(ative)
                        break
                    
    def Update(self):
        # -- Faz as atualizações na tela -- 
        for elemento in self.copia:
            for celulas in self.Celulas:
                if celulas.celula == elemento:
                    if celulas.state:
                        celulas.Ativa()
                    else:
                        celulas.Desativa()
                    
                    self.copia.remove(elemento)
                    break
        
        self.inst.after(10, self.Update)

    def ChecaVida(self):
        indices = []
        
        for celula in self.Celulas:
            if celula.state == True:
                indices.append(self.Celulas.index(celula))
        
        quant_x = self.res_x//self.tamanho
        quant_y = self.res_y//self.tamanho

        for i in indices:
            ...    
            
    

# Inicia o game
resolucao = '1020x760'
Jogo(resolucao)