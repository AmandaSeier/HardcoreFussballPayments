# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Indbetal").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

        # hvem betaler?
        # hvordan skal de betale?
            # måske input felter?
            # eller vis en liste der viser en oversigt over medlemmerne?

        # name validation
            # tjek om navnet står i dictet
            # sørg for at tjekke store og små forbogstaver og mellemrum etc

        # payment and money validation
            # skal gemmes og opdateres in real time
            # tjek korresponderende value til key i dict


    def addMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        self.master.gemFilen()

