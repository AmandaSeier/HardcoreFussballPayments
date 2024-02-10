from tkinter import *

class Info:
    def __init__(self, master):
        self.master = master
        self.infoWindow = Toplevel(self.master)
        self.infoWindow.geometry("600x300")
        self.infoWindow.minsize(width=600, height=300)
        self.infoWindow.maxsize(width=600, height=300)
        self.infoWindow.title("Information")

        title = Label(self.infoWindow, text="INFORMATION", font=("Impact", 40), fg="#00A878")
        title.pack()

if __name__ == "__main__":
    root = Tk()
    app = Info(root)
    root.mainloop()
