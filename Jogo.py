from Tela import Tela
from Tile import Tile

from tkinter import *

class Jogo(Tela):
    def __init__(self, resolucao):
        # Inicia o objeto Tela
        Tela.__init__(self, resolucao)

        # Inicia a Updatar a Tela
        self.Update()
        
        # Os bingings
        self.inst.bind('<Button-1>', self.OnClick)

        # Essa instancia usada vem do objeto Tela
        self.inst.focus_force()
        self.inst.mainloop()

    def OnClick(self, event):
        coord = (event.x, event.y)
        elemento = self.canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1])

        if len(elemento) >= 1:
            for i in range(len(self.Tiles)):
                if self.Tiles[i].tile == elemento[0]:
                    self.Tiles[i].Gerencia()
                    break
                    
    def Update(self):
        for e in self.Tiles:
            if e.state == False:
                e.Desativa()
            else:
                e.Ativa()

        self.inst.after(10, self.Update)
    

# Inicia o game
resolucao = '1020x760'
Jogo(resolucao)