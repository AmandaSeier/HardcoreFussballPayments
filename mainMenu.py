# import af libraries, classes og funktioner fra andre filer
from tkinter import *
from tkinter import messagebox
from indbetalingsliste import Indbetalingsliste
from indbetal import Indbetal
from information import Info
import fodboldturV2

# main window  ***
class MainWindow:
    def __init__(self):
        self.total = 1200
        self.target = 4500
        self.root = Tk()

        # laver vinduet og dets størrelse
        self.root.geometry("700x480")
        self.root.minsize(width=700, height=480)
        self.root.maxsize(width=700, height=480)
        self.root.title("Fodboldtur")

        # prøver at loade pickle-filen med dictet
        try:
            self.fodboldtur = fodboldturV2.load_data('dict/betalinger.pk')
        # hvis dette ikke kan lade sig gøre = error
        except FileNotFoundError:
            messagebox.showerror(parent=self.root, title="Error", message="Filen blev ikke fundet")
            self.fodboldtur = {}

        # vindue titel
        title = Label(self.root, text="FODBOLDTUR", font=("Impact", 100), fg="#00A878")
        title.pack()

        # laver en lille velkomst besked
        welcome = Label(self.root, text="Velkommen til klubbens betalingsoversigt til England, hvordan ønsker du at forsætte herfra?")
        welcome.pack(pady=17)

        # variabler til knapper
        buttonPaddingY = 5
        buttonPaddingX = 20
        buttonWidth = 25
        buttonHeight = 3

        # betalingsliste knap
        listButton = Button(self.root, text="Betalingsliste", command=self.open_indbetalingsliste, height=buttonHeight, width=buttonWidth)
        listButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # betalingsknap
        payButton = Button(self.root, text="Lav indbetaling", command=self.open_indbetal, height=buttonHeight, width=buttonWidth)
        payButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # informationsknap
        infoButton = Button(self.root, text="Information", command=self.open_info, height=buttonHeight, width=buttonWidth)
        infoButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # exit knap (lukker programmet)
        exitButton = Button(self.root, text="Afslut", command=self.root.quit, height=buttonHeight, width=buttonWidth)
        exitButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        self.root.mainloop()

    # funktion der åbner indbetalingsliste
    def open_indbetalingsliste(self):
        try:
            self.fodboldtur = fodboldturV2.load_data('dict/betalinger.pk')
        except FileNotFoundError:
            messagebox.showerror(parent=self.root, title="Error", message="Filen blev ikke fundet")
            self.fodboldtur = {}
        app = Indbetalingsliste(self.root, self.fodboldtur)

    # funktion der åbner indbetalingsvinduet
    def open_indbetal(self):
        Indbetal(self.root)

    # funktion der åbner informationsvinduet
    def open_info(self):
        Info(self.root)

# main loop
if __name__ == '__main__':
    main = MainWindow()
