from tkinter import *
from pl.form import Rigester



if __name__ == "__main__":
    screen=Tk()
    PageMe=Rigester.App(screen)
    screen.geometry("%dx%d+%d+%d" % (1920, 1000, -10, -2))
    screen.title("Restaurant Management")
    screen.iconbitmap("img/icon.ico")
    screen.resizable(False, False)
    screen.mainloop()