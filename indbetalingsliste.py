# LAVET MED EN SMULE HJÆLP FRA STOFFER, JOPPER OG CHAD (DOG MED NOGLE MODIFICATIONS)
# import af libraries
from tkinter import *
from tkinter import ttk
import pickle

# indbetalingsliste class
class Indbetalingsliste:
    def __init__(self, master, data):
        self.master = master
        self.listWindow = Toplevel(self.master)
        self.listWindow.geometry("400x240")
        self.listWindow.maxsize(width=400, height=240)
        self.listWindow.minsize(width=400, height=240)
        self.listWindow.title("Betalingsliste")     # titlen på vinduet

        # overskriften til vinduet
        title = Label(self.listWindow, text="INDBETALINGSLISTE", font=("Impact", 40), fg="#00A878")
        title.pack()

        # bruger treeview-widget'en og laver to kolonner (hhv. navn og beløb)
        self.tree = ttk.Treeview(self.listWindow, columns=("FULDE NAVN", "BETALT BELØB"), show="headings")

        # sætter overskrifterne til kolonnerne
        self.tree.heading("FULDE NAVN", text="FULDE NAVN")
        self.tree.heading("BETALT BELØB", text="BETALT BELØB")

        # indsætter data fra dict i "treeview"
        self.insert_data(data)

        self.tree.pack(expand=True, fill="both")

    # funktion der indsætter dataen
    def insert_data(self, data):
        self.tree.delete(*self.tree.get_children())

        # tjekker data i dict'et og plotter det i treeview
        for key, value in data.items():
            value_str = str(value)
            values = [value_str] if not isinstance(value, (list, tuple)) else value
            self.tree.insert("", "end", values=(key,) + tuple(values))

        # ændrer overskrifterne og data, så det er centreret
        for column in self.tree["columns"]:
            self.tree.heading(column, anchor="center")
            self.tree.column(column, anchor="center")

# funktion der indlæser indholdet af fodboldtur
def load_data(filename: str) -> dict:
    try:
        with open(filename, "rb") as infile:
            fodboldtur = pickle.load(infile)
            # her tjekkes der om værdierne er floats (hvis de er, så konverteres de til en liste
            for key, value in fodboldtur.items():
                if isinstance(value, float):
                    fodboldtur[key] = [value]

    # error hvis filen ikke blev fundet
    except FileNotFoundError:
        print("Filen blev ikke fundet")
        fodboldtur = {}

    return fodboldtur

# funktion der åbner indbetalingsliste
def open_indbetalingsliste():
    filename = 'dict/betalinger.pk'
    fodboldtur = load_data(filename)

    # laver et vindue og loader indholdet
    root = Tk()
    app = Indbetalingsliste(root, fodboldtur)
    root.mainloop()

# kører åbningen af indbetalingslisten
if __name__ == "__main__":
    open_indbetalingsliste()
