from tkinter import *
from Tile import Tile

# A classe responsável pela criação da Tela
class Tela():
    def __init__(self, resolucao:str):
        self.inst = Tk()
        self.inst['bg'] = 'black'
        self.inst.attributes('-fullscreen', True) 
        font = ('Small Fonts', 30, 'bold')

        # Obtém a resolução informada e transforma em valores úteis
        res_x, res_y = resolucao.split('x')
        res_x = int(res_x); res_y = int(res_y)

        # ------------------------------------------------
        # -- CANVAS --
        # O canvas usado
        self.canvas = Canvas(self.inst, background='black', highlightthickness=0
        , width=res_x, height=res_y-80)
        
        # Cria os Tiles
        self.Tiles = []

        for x in range(0, res_x, 20):
            for y in range(0, res_y-80, 20):
                self.Tiles.append(Tile(((x, y), (x+20, y+20)), self.canvas, self.inst))

        # -------------------
        # -- BOTÃO -- 
        self.but = Button(self.inst, bg='darkgray', fg='white', text='Sair',
         command=exit, highlightthickness=0, relief='flat', width=100, font=font)

        # ------------------------------------------------
        
        # Empacota
        self.canvas.pack()
        self.but.pack()