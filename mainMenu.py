# GUI WITH TKINTER - FODBOLD SOMETHING

# importing libraries
from tkinter import *
from indbetalingsliste import Indbetalingsliste
from leaderboard import Leaderboard
from indbetal import Indbetal

buttonPaddingY = 10
buttonPaddingX = 20
buttonWidth = 15
buttonHeight = 2

class MainWindow:
    def __init__(self):
        self.total = 1200
        self.target = 4500
        self.root = Tk()

        # Creating the window
        self.root.geometry("800x500")
        self.root.minsize(width=800, height=500)
        self.root.maxsize(width=800, height=500)
        self.root.title("Fodboldtur")

        # Menu title
        title = Label(self.root, text="FODBOLDTUR", font=("Impact", 100), fg="#00A878")
        title.pack()

        welcome = Label(self.root, text="Velkommen til fodbold klubbens tur til England, hvordan ønsker du at forsætte herfra?")
        welcome.pack(pady=15)

        # "Betalinger" button
        listButton = Button(self.root, text="Betalingsliste", command=lambda: Indbetalingsliste(self), height=buttonHeight, width=buttonWidth)
        listButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # "Indbetal" button
        payButton = Button(self.root, text="Administrer betaling", command=lambda: Indbetal(self), height=buttonHeight, width=buttonWidth)
        payButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # "Leaderboard" button
        leaderboardButton = Button(self.root, text="Leaderboard", command=lambda: Leaderboard(self), height=buttonHeight, width=buttonWidth)
        leaderboardButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        # "Exit" button
        exitButton = Button(self.root, text="Afslut", command=quit, height=buttonHeight, width=buttonWidth)
        exitButton.pack(padx=buttonPaddingX, pady=buttonPaddingY, side=TOP)

        mainloop()

if __name__ == '__main__':
    main = MainWindow()
