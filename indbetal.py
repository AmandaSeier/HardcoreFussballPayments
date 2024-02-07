from tkinter import *

class Indbetal:
    def __init__(self, master):
        self.master = master
        self.indbetalWindow = Toplevel(self.master.root)
        self.indbetalWindow.geometry("600x300")
        self.indbetalWindow.minsize(width=600, height=300)
        self.indbetalWindow.maxsize(width=600, height=300)
        self.indbetalWindow.title("Administrer betalinger")