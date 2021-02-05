from tkinter import *

# O Tile que você fica clicando nele
class Tile():
    def __init__(self, coordenadas, canvas, tk): 
        # Cria o Tile no Canvas
        self.C = canvas
        self.tile = self.C.create_rectangle(coordenadas[0], coordenadas[1], fill='gray', outline='black')
        self.state = False

    # Ativa e desativa o Tile
    def Ativa(self):
        self.C.itemconfig(self.tile, fill='yellow')
    def Desativa(self):
        self.C.itemconfig(self.tile, fill='gray')

    def Gerencia(self):
        if self.state:
            self.state = False
        else:
            self.state = True

        
