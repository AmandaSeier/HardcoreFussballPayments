# importerer libraries og filer
from tkinter import *
import tkinter as tk
from fodboldturV2 import fodboldtur, load_data

# INDBETAL CLASS
class Indbetal:
    def __init__(self, master):
        self.master = master
        self.indbetalWindow = Toplevel(self.master)
        self.indbetalWindow.geometry("500x200")     # vindue størrelse
        self.indbetalWindow.minsize(width=500, height=200)     # min størrelse af vindue
        self.indbetalWindow.maxsize(width=500, height=200)     # max størrelse af vindue
        self.indbetalWindow.title("Lav indbetaling")      # laver titel på vindue
        # fixer størrelse på input feltet, dets placering og udseende
        self.indbetalWindow.grid_columnconfigure(0, weight=1)
        self.indbetalWindow.grid_columnconfigure(1, weight=1)
        self.indbetalWindow.grid_rowconfigure(0, weight=1)
        self.indbetalWindow.grid_rowconfigure(5, weight=1)
        self.fornavn = tk.StringVar()
        self.efternavn = tk.StringVar()

        stretch_label = tk.Label(self.indbetalWindow, text="")
        stretch_label.grid(row=0, column=0)

        # overskrift i vinduet :J
        title = Label(self.indbetalWindow, text="LAV INDBETALING", font=("Impact", 40), fg="#00A878")
        title.grid(row=0, column=0, columnspan=2, pady=0)

        # inputfelt til fornavn
        name_label = tk.Label(self.indbetalWindow, text='Fornavn')
        name_label.grid(row=1, column=0)

        name_entry = tk.Entry(self.indbetalWindow, textvariable=self.fornavn)
        name_entry.grid(row=1, column=1)

        # inputfelt til efternavn
        passw_label = tk.Label(self.indbetalWindow, text='Efternavn')
        passw_label.grid(row=2, column=0)

        passw_entry = tk.Entry(self.indbetalWindow, textvariable=self.efternavn)
        passw_entry.grid(row=2, column=1)

        # næste knap
        sub_btn = tk.Button(self.indbetalWindow, text='Næste', command=self.valider)
        sub_btn.grid(row=3, column=1)

        # pinter dictet (debugging)
        print("Dict: ")
        print(load_data('dict/betalinger.pk'))

    # funktion der validerer input navnet
    def valider(self):
        fornavn = self.fornavn.get().strip().lower()  # konverter inputnavnet til lowercase
        efternavn = self.efternavn.get().strip().lower()  # konverter inputnavnet til lowercase
        # ændrer navnet, så det starter med store bogstaver
        fuldtNavn = f"{fornavn.capitalize()} {efternavn.capitalize()}"
        print(f"Inputnavn: \"{fuldtNavn}\" ")
        # udskriver navnene i dictionariet (debugging)
        print("Dict names:", list(fodboldtur.keys()))
        if fuldtNavn in fodboldtur:
            print(f"Navnet {fuldtNavn} findes")     # printes hvis det findes i dict
        else:
            print(f"Navnet {fuldtNavn} findes ikke")    # printes hvis det ikke findes i dict


if __name__ == "__main__":
    root = Tk()
    app = Indbetal(root)
    root.mainloop()
