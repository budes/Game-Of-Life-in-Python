from tkinter import *

# A celula que você fica clicando nela
class Celula():
    def __init__(self, coordenadas:tuple, canvas): 
        # Cria a celula no Canvas
        self.C = canvas
        self.celula = self.C.create_rectangle(coordenadas[0], coordenadas[1], fill='gray', outline='black')
        self.state = False

    # Ativa e desativa a celula
    def Ativa(self):
        self.C.itemconfig(self.celula, fill='white')
    def Desativa(self):
        self.C.itemconfig(self.celula, fill='gray')

    def Gerencia(self, ativar:bool):
        # Troca o state de acordo com o que é chamado
        if self.state == False and ativar:
            self.state = True
        elif self.state == True and not ativar:
            self.state = False

        
