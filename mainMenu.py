# import af libraries, classes og funktioner fra andre filer
from tkinter import *
from tkinter import messagebox
from indbetalingsliste import Indbetalingsliste
from leaderboard import Leaderboard
from indbetal import Indbetal
from information import Info
import fodboldturV2

# main window class
class MainWindow:
    def __init__(self):
        self.total = 1200
        self.target = 4500
        self.root = Tk()

        self.root.geometry("800x500")
        self.root.minsize(width=800, height=560)
        self.root.maxsize(width=800, height=560)
        self.root.title("Fodboldtur")

        try:
            self.fodboldtur = fodboldturV2.load_data()
        except FileNotFoundError:
            messagebox.showerror(parent=self.root, title="Error", message="Filen blev ikke fundet")
            self.fodboldtur = {}

        title = Label(self.root, text="FODBOLDTUR", font=("Impact", 100), fg="#00A878")
        title.pack()

        welcome = Label(self.root, text="Velkommen til klubbens betalingsoversigt til England, hvordan ønsker du at forsætte herfra?")
        welcome.pack(pady=17)

        buttonPaddingY = 5
        buttonPaddingX = 20
        buttonWidth = 25
        buttonHeight = 3

        listButton = Button(self.root, text="Betalingsliste", command=self.open_indbetalingsliste, height=buttonHeight, width=buttonWidth)
        listButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        payButton = Button(self.root, text="Administrer betaling", command=self.open_indbetal, height=buttonHeight, width=buttonWidth)
        payButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        leaderboardButton = Button(self.root, text="Leaderboard", command=self.open_leaderboard, height=buttonHeight, width=buttonWidth)
        leaderboardButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        infoButton = Button(self.root, text="Information", command=self.open_info, height=buttonHeight, width=buttonWidth)
        infoButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        exitButton = Button(self.root, text="Afslut", command=self.root.quit, height=buttonHeight, width=buttonWidth)
        exitButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        self.root.mainloop()

    def open_indbetalingsliste(self):
        try:
            self.fodboldtur = fodboldturV2.load_data()
        except FileNotFoundError:
            messagebox.showerror(parent=self.root, title="Error", message="Filen blev ikke fundet")
            self.fodboldtur = {}

        app = Indbetalingsliste(self.root, self.fodboldtur)

    def open_indbetal(self):
        Indbetal(self.root)

    def open_leaderboard(self):
        Leaderboard(self.root)

    def open_info(self):
        Info(self.root)

if __name__ == '__main__':
    main = MainWindow()
