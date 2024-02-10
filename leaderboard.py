from tkinter import *

class Leaderboard:
    def __init__(self, master):
        self.master = master
        self.leaderboardWindow = Toplevel(self.master)
        self.leaderboardWindow.geometry("600x300")
        self.leaderboardWindow.minsize(width=600, height=300)
        self.leaderboardWindow.maxsize(width=600, height=300)
        self.leaderboardWindow.title("Leaderboard")

        title = Label(self.leaderboardWindow, text="LEADERBOARD", font=("Impact", 40), fg="#00A878")
        title.pack()

if __name__ == "__main__":
    root = Tk()
    app = Leaderboard(root)
    root.mainloop()
