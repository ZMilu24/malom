from tkinter import *
from dot import Dot

class GameScreen():
    def __init__(self, winsize = 500):

        # global game variables
        self.gameState = 0  # 0 - start ; 1 - middle game ; 2 - endgame ; 3 - winner screen
        self.nexdtMove = "white"
        self.winner = None

        self.root = Tk()
        self.root.minsize(winsize,winsize)
        self.root.maxsize(winsize,winsize)
        self.root.geometry("500x500")
        self.canvas = Canvas(self.root, width=500, height=500, bg="grey")

        self.mainText()

        innerLayer = [
                            [Dot([200,200], self.canvas), Dot([250,200], self.canvas), Dot([300,200], self.canvas)],
                            Dot([200,250], self.canvas),                                Dot([300,250], self.canvas),
                            [Dot([200,300], self.canvas), Dot([250,300], self.canvas), Dot([300,300], self.canvas)],
        ]
        middleLayer = [
                            [Dot([150,150], self.canvas), Dot([250,150], self.canvas), Dot([350,150], self.canvas)],
                            Dot([150,250], self.canvas),                                Dot([350,250], self.canvas),
                            [Dot([150,350], self.canvas), Dot([250,350], self.canvas), Dot([350,350], self.canvas)],
        ]
        outherLayer = [
                            [Dot([100,100], self.canvas), Dot([250,100], self.canvas), Dot([400,100], self.canvas)],
                            Dot([100,250], self.canvas),                                Dot([400,250], self.canvas),
                            [Dot([100,400], self.canvas), Dot([250,400], self.canvas), Dot([400,400], self.canvas)],
        ]

        gameMap = [innerLayer, middleLayer, outherLayer]

        self.canvas.pack()
        self.root.mainloop()

    def mainText(self, txt = None):
        if txt == None:
            txt = "Next move: "+self.nexdtMove
        self.gameText = Label(self.root, text=txt)
        self.gameText.pack()