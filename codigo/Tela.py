from tkinter import *
from Celula import Celula

# A classe responsável pela criação da Tela
class Tela():
    def __init__(self, resolucao:str):
        self.inst = Tk()
        self.inst['bg'] = 'black'
        self.inst.attributes('-fullscreen', True) 
        font = ('Small Fonts', 30, 'bold')

        # Obtém a resolução informada e transforma em valores úteis
        self.res_x, self.res_y = resolucao.split('x')
        self.res_x = int(self.res_x); self.res_y = int(self.res_y)

        # ------------------------------------------------
        # -- CANVAS --
        # O canvas usado
        self.canvas = Canvas(self.inst, background='black', highlightthickness=0
        , width=self.res_x, height=self.res_y-80)
        
        # Cria as celulas na Tela
        self.Celulas = []
        self.tamanho = 20

        for x in range(0, self.res_x, self.tamanho):
            for y in range(0, self.res_y-80, self.tamanho):
                self.Celulas.append(Celula(((x, y), (x+self.tamanho, y+self.tamanho)), self.canvas))

        # -------------------
        # -- BOTÃO -- 
        self.but = Button(self.inst, bg='darkgray', fg='white', text='Sair',
         command=exit, highlightthickness=0, relief='flat', width=100, font=font)

        # ------------------------------------------------
        
        # Empacota
        self.canvas.pack()
        self.but.pack()