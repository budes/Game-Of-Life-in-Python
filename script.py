from tkinter import *

# A classe responsável pela criação da Tela
class Tela():
    def __init__(self, resolucao:str):
        self.inst = Tk()
        self.inst['bg'] = 'black' 

        # Obtém a resolução informada e transforma em valores úteis
        res_x, res_y = resolucao.split('x')
        res_x = int(res_x); res_y = int(res_y)

        # O canvas usado
        self.canvas = Canvas(self.inst, background='black', highlightthickness=0
        , width=res_x, height=res_y-100)
        
        # Cria os Tiles
        self.Tiles = []

        for x in range(0, res_x, 20):
            for y in range(0, res_y-100, 20):
                self.Tiles.append(Tile(((x, y), (x+20, y+20)), self.canvas, self.inst))

        # Empacota e faz 
        self.canvas.pack()
        self.inst.mainloop()

# O Tile que você fica clicando nele
class Tile():
    def __init__(self, coordenadas, canvas, tk): 
        # Cria o Tile no Canvas
        self.C = canvas
        self.C.create_rectangle(coordenadas[0], coordenadas[1], fill='gray', outline='black', tag='tile')
        self.state = False

    # Ativa e desativa o Tile
    def Ativa(self):
        self.C.itemconfig('tile', fill='yellow')
        return True
    def Desativa(self):
        self.C.itemconfig('tile', fill='gray')
        return False

    def Gerencia(self):
        if self.state:
            self.state = False
        else:
            self.state = True


class Jogo(Tela):
    def __init__(self, resolucao):

        Tela.__init__(self, resolucao)
        
        print(Tela)


# Inicia o game
resolucao = '1020x760'
Jogo(resolucao)