from Tela import Tela
from Tile import Tile

from tkinter import *

class Jogo(Tela):
    def __init__(self, resolucao):
        # Inicia o objeto Tela
        Tela.__init__(self, resolucao)
        
        # Armazena a copia das instancias
        self.copia = []

        # Os bingings
        self.inst.bind(('<Button-1>', '<B1-Motion>'), self.OnClick)
        
        # Inicia a Updatar a Tela
        self.Update()

        # Essa instancia usada vem do objeto Tela
        self.inst.focus_force()
        self.inst.mainloop()

    def OnClick(self, event):
        # -- Quando Clicar -- 
        coord = (event.x, event.y)
        elemento = self.canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1])

        print(coord)

        if len(elemento) >= 1:
            if (elemento[0] in self.copia) or len(self.copia) == 0:
                self.copia.append(elemento[0])
                for i in range(len(self.Tiles)):
                    if self.Tiles[i].tile == elemento[0]:
                        self.Tiles[i].Gerencia()
                        break
                    
    def Update(self):
        for elemento in self.copia:
            for tiles in self.Tiles:
                if tiles.tile == elemento:
                    if tiles.state:
                        tiles.Ativa()
                    else:
                        tiles.Desativa()
                    
                    self.copia.remove(elemento)
                    break
        
        self.inst.after(50, self.Update)
    

# Inicia o game
resolucao = '1020x760'
Jogo(resolucao)