# importing tkinter module
from tkinter import *
from PIL import ImageTk, Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()

        img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
        panel = Label(self.listWindow, image=img)
        panel.image = img
        panel.pack(side="bottom", fill="both", expand="yes")

        # load pickle fil
            # pickle-fil error handling? - hvis filen ikke findes eller loades korrekt

        # måske kunne man endda lave en liste, hvorpå der er forskellige knapper, som man kan bruge til at
        # sortere betalingerne efter forskellige faktorer.på den måde kan man smelte leaderboard vinduet
        # sammen med selve listen.

        # plot data fra dict (keys og values)

        # knap til sortering (mest-mindst)?

        # knap til sortering (mindst-mest)?