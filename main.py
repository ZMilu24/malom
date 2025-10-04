from tkinter import *
from game import GameScreen

def main():
    root = Tk()

    #main screen
    title = Label(root, text="Nine Men's Morris")
    title.place(rely=0)

    welcome = Label(root, text='Wellcome to the Game')
    welcome.place(rely=.1)

    TPButton = Button(root, text="2 player game", command=lambda : GameScreen())
    TPButton.place(rely=.2)

    root.minsize(800, 800)
    root.maxsize(800, 800)

    root.mainloop()

main()