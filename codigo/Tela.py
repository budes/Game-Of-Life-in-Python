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
        res_x, res_y = resolucao.split('x')
        res_x = int(res_x); res_y = int(res_y)

        # ------------------------------------------------
        # -- CANVAS --
        # O canvas usado
        self.canvas = Canvas(self.inst, background='black', highlightthickness=0
        , width=res_x, height=res_y-80)
        
        # Cria as celulas na Tela
        self.Celulas = []
        tamanho = 20

        '''
        for x in range(0, res_x, tamanho):
            for y in range(0, res_y-80, tamanho):
                self.Celulas.append(Celula(((x, y), (x+tamanho, y+tamanho)), self.canvas))'''

        for y in range(0, res_y-80, tamanho):
            aux = []
            for x in range(0, res_x, tamanho):
                aux.append(Celula(((x, y), (x+tamanho, y+tamanho)), self.canvas))
            
            self.Celulas.append(aux)

        # -------------------
        # -- BOTÃO -- 
        framebut = Frame(self.inst, bg='darkgray')
        
        but = Button(framebut, bg='darkgray', fg='white', text='SAIR',
         command=exit, highlightthickness=0, relief='flat', width=20, font=font)
        self.butjogo = Button(framebut, bg='darkgray', fg='white', text='INICIAR',
         command=exit, highlightthickness=0, relief='flat', width=20, font=font)

        # ------------------------------------------------
        
        # Empacota
        self.canvas.pack()

        framebut.pack()
        but.pack(side=RIGHT)
        self.butjogo.pack(side=RIGHT)