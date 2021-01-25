from tkinter import *

class PyCalculator:
    def __init__(self, master=None):
        self.mainwindow = Frame(master)
        self.mainwindow.pack()


root = Tk()
root.title("Python Calculator")
root.geometry("250x250")
PyCalculator(root)
root.mainloop()