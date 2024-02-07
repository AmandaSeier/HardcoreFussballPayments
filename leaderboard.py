from tkinter import *

class Leaderboard:
    def __init__(self, master):
        self.master = master
        self.leaderboardWindow = Toplevel(self.master.root)
        self.leaderboardWindow.geometry("600x300")
        self.leaderboardWindow.minsize(width=600, height=300)
        self.leaderboardWindow.maxsize(width=600, height=300)
        self.leaderboardWindow.title("Leaderboard")