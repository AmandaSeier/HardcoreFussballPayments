from tkinter import *

class Indbetal:
    def __init__(self, master):
        self.master = master
        self.indbetalWindow = Toplevel(self.master)
        self.indbetalWindow.geometry("600x300")
        self.indbetalWindow.minsize(width=600, height=300)
        self.indbetalWindow.maxsize(width=600, height=300)
        self.indbetalWindow.title("Administrer betalinger")

        title = Label(self.indbetalWindow, text="BETALINGER", font=("Impact", 40), fg="#00A878")
        title.pack()

if __name__ == "__main__":
    root = Tk()
    app = Indbetal(root)
    root.mainloop()
