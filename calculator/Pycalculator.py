from tkinter import *

class PyCalculator:
    def __init__(self, master=None):
        
        # Criação do frame do programa que suportará os elementos
        self.mainwindow = Frame(master)
        self.mainwindow.pack()


        # Criação da tela de calculo.
        self.calcwindow = Canvas(self.mainwindow, bg="white")
        self.calcwindow["height"] = 20
        self.calcwindow["width"] = 230
        self.calcwindow.pack()

        # Criação do texto da tela de calculo
        self.calctext = Label(self.mainwindow)
        self.calctext["text"] = "123"
        self.calctext.pack(side=RIGHT)

        # Criação do frame que segura os botoes do lado esquerdo da tela
        self.lftbtns = Frame(self.mainwindow)
        self.lftbtns.pack(side=LEFT)

        #CRIAÇÃO DOS BOTOES

        self.btnseven = Button(self.mainwindow)




#Iniciação
root = Tk()
root.title("Python Calculator")
root.geometry("250x200")
PyCalculator(root)
root.mainloop()