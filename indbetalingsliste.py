from tkinter import *

class Indbetalingsliste:
    def __init__(self, master):
        self.master = master
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.geometry("600x300")
        self.listWindow.minsize(width=600, height=300)
        self.listWindow.maxsize(width=600, height=300)
        self.listWindow.title("Indbetalinger")
