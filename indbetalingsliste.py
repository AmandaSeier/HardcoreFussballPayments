# importing libraries and files
from tkinter import *
from tkinter import ttk
import pickle

# INDBETALINGS CLASS
class Indbetalingsliste:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.listWindow = Toplevel(self.master)
        self.listWindow.geometry("390x320")     # vindue størrelse
        self.listWindow.maxsize(width=390, height=320)      # min. vindue størrelse
        self.listWindow.minsize(width=390, height=320)      # max. vindue størrelse
        self.listWindow.title("Betalingsliste")     # laver titel på vindue
        title = Label(self.listWindow, text="INDBETALINGSLISTE", font=("Impact", 45), fg="#00A878")     # oveskrift
        title.pack()    # plotter det i vinduet

        # tree-view listen med navne
        self.tree = ttk.Treeview(self.listWindow, columns=("FULDE NAVN", "BETALT BELØB"), show="headings")
        self.tree.heading("FULDE NAVN", text="FULDE NAVN")
        self.tree.heading("BETALT BELØB", text="BETALT BELØB")
        self.insert_data(data)
        self.tree.pack(expand=False, fill="both")

        Label(self.listWindow, text="").pack(side=LEFT, padx=3)

        # knapper der sortere data
        højestKnap = Button(self.listWindow, text="Mangler mindst", command=self.højest)
        højestKnap.pack(side=LEFT, padx=3)

        lavestKnap = Button(self.listWindow, text="Mangler mest", command=self.lavest)
        lavestKnap.pack(side=LEFT, padx=3)

        alfabetiskKnap = Button(self.listWindow, text="Alfabetisk", command=self.alfabetisk)
        alfabetiskKnap.pack(side=LEFT, padx=3)

    def insert_data(self, data):
        # fjerner data fra tree-view
        self.tree.delete(*self.tree.get_children())
        # indsætter data deri
        for key, value in data.items():
            value_str = str(value)
            values = [value_str] if not isinstance(value, (list, tuple)) else value
            self.tree.insert("", "end", values=(key,) + tuple(values))
        # justere overskrifter og data i tabellen
        for column in self.tree["columns"]:
            self.tree.heading(column, anchor="center")
            self.tree.column(column, anchor="center")

    def højest(self):
        # sortere data efter betalt beløb (højest først)
        sorteretData = sorted(self.data.items(), key=lambda x: x[1][0] if isinstance(x[1], list) else x[1], reverse=True)
        self.insert_data(dict(sorteretData))

    def lavest(self):
        # sortere data efter betalt beløb (lavest først)
        sorteretData = sorted(self.data.items(), key=lambda x: x[1][0] if isinstance(x[1], list) else x[1])
        self.insert_data(dict(sorteretData))

    def alfabetisk(self):
        # sortere data alfabetisk efter navn
        sorteretData = sorted(self.data.items())
        self.insert_data(dict(sorteretData))

# funktion der loader filen med dictet
def load_data(filename: str) -> dict:
    try:
        with open(filename, "rb") as infile:
            # indlæser data fra pickle-filen
            fodboldtur = pickle.load(infile)
            for key, value in fodboldtur.items():
                if isinstance(value, float):
                    fodboldtur[key] = [value]
    except FileNotFoundError:
        print("Filen blev ikke fundet")
        fodboldtur = {}
    return fodboldtur

def open_indbetalingsliste():
    filename = 'dict/betalinger.pk'
    # indlæser data og åbner indbetalingsliste-vinduet
    fodboldtur = load_data(filename)
    root = Tk()
    app = Indbetalingsliste(root, fodboldtur)
    root.mainloop()

if __name__ == "__main__":
    open_indbetalingsliste()
