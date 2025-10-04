from tkinter import *
from dot import Dot

class GameScreen():
    def __init__(self, winsize = 800):

        # global game variables
        self.gameState = 0  # 0 - start ; 1 - middle game ; 2 - endgame ; 3 - winner screen
        self.nexdtMove = "white"
        self.winner = None
        self.gameText = None
        self.whiteRingsOnMap = 0
        self.blackRingsOnMap = 0
        self.whiteRingsOffMap = 9
        self.blackRingsOffMap = 9


        #create game map
        self.root = Tk()
        self.root.minsize(winsize,winsize)
        self.root.maxsize(winsize,winsize)
        self.root.geometry("800x800")
        self.canvas = Canvas(self.root, width=800, height=800, bg="grey")

        innerLayer = [
                            Dot([300,300], self.canvas, self), Dot([400,300], self.canvas, self), Dot([500,300], self.canvas, self),
                            Dot([300,400], self.canvas, self),                                    Dot([500,400], self.canvas, self),
                            Dot([300,500], self.canvas, self), Dot([400,500], self.canvas, self), Dot([500,500], self.canvas, self),
        ]
        middleLayer = [
                            Dot([200,200], self.canvas, self), Dot([400,200], self.canvas, self), Dot([600,200], self.canvas, self),
                            Dot([200,400], self.canvas, self),                                    Dot([600,400], self.canvas, self),
                            Dot([200,600], self.canvas, self), Dot([400,600], self.canvas, self), Dot([600,600], self.canvas, self),
        ]
        outherLayer = [
                            Dot([100,100], self.canvas, self), Dot([400,100], self.canvas, self), Dot([700,100], self.canvas, self),
                            Dot([100,400], self.canvas, self),                                    Dot([700,400], self.canvas, self),
                            Dot([100,700], self.canvas, self), Dot([400,700], self.canvas, self), Dot([700,700], self.canvas, self),
        ]

        self.gameMap = [innerLayer, middleLayer, outherLayer]

        for layer in range(len(self.gameMap)):
            for i in range(len(self.gameMap[layer])):
                nodes = []
                if (i == 0):
                    nodes.append(self.gameMap[layer][1])
                    nodes.append(self.gameMap[layer][3])
                elif (i == 3):
                    nodes.append(self.gameMap[layer][0])
                    nodes.append(self.gameMap[layer][5])
                    if (layer == 1):
                        nodes.append(self.gameMap[layer+1][3])
                        nodes.append(self.gameMap[layer-1][3])
                elif (i == 4):
                    nodes.append(self.gameMap[layer][2])
                    nodes.append(self.gameMap[layer][7])
                    if (layer == 1):
                        nodes.append(self.gameMap[layer+1][4])
                        nodes.append(self.gameMap[layer-1][4])
                elif (i == 7):
                    nodes.append(self.gameMap[layer][4])
                    nodes.append(self.gameMap[layer][6])
                elif (i == 2):
                    nodes.append(self.gameMap[layer][1])
                    nodes.append(self.gameMap[layer][4])
                elif (i == 5):
                    nodes.append(self.gameMap[layer][6])
                    nodes.append(self.gameMap[layer][3])
                else:
                    nodes.append(self.gameMap[layer][i+1])
                    nodes.append(self.gameMap[layer][i-1])
                    if (layer == 1):
                        if (i == 1):
                            nodes.append(self.gameMap[layer+1][1])
                            nodes.append(self.gameMap[layer-1][1])
                        elif (i == 6):
                            nodes.append(self.gameMap[layer+1][6])
                            nodes.append(self.gameMap[layer-1][6])
                self.gameMap[layer][i].setNext(nodes)

        self.canvas.pack()

        self.mainText()

        self.root.mainloop()

    def mainText(self, txt = None):
        if (self.gameText != None):
            self.gameText.pack_forget()
        if txt == None:
            txt = "Next move: "+self.nexdtMove
        self.gameText = Label(self.root, text=txt)
        self.gameText.pack()

    def buttonGetClicked(dot):
        print("dot get clicked")