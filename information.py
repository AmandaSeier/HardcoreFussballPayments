# importing libraries
from tkinter import *

# INFORMATION CLASS
class Info:
    def __init__(self, master):
        self.master = master
        self.infoWindow = Toplevel(self.master)
        self.infoWindow.geometry("500x200")     # størrelse på vindue
        self.infoWindow.minsize(width=500, height=200)     # mindste størrelse på vindue
        self.infoWindow.maxsize(width=500, height=200)     # maksimale størrelse på vindue
        self.infoWindow.title("Information")       # vindue titel
        title = Label(self.infoWindow, text="INFORMATION", font=("Impact", 40), fg="#00A878") # vindue overskrift
        title.pack()    # plotter titlen i vinduet

        # information omkring turen
        information = Label(self.infoWindow,
                            text="Denne gang går turen til Wembley Stadium. Dette stadion er et af Europas\n"
                                 "største. Det er netop her turen går hen sommeren 2024, når England skal\n"
                                 "spille på hjemmebane mod Island i Europamesterskaberne. Denne tur er\n"
                                 "sammen arrangeret af klubbens formand (Ole Olesen), da der var stor\n"
                                 "stemning for at se lige netop denne kamp.", justify="left", pady=10)

        # plotter informationsteksten i vinduet nedenunder overskriften i vinduet
        information.pack()


if __name__ == "__main__":
    root = Tk()
    app = Info(root)
    root.mainloop()
