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
                            Dot([200,200], self.canvas), Dot([250,200], self.canvas), Dot([300,200], self.canvas),
                            Dot([200,250], self.canvas),                                Dot([300,250], self.canvas),
                            Dot([200,300], self.canvas), Dot([250,300], self.canvas), Dot([300,300], self.canvas),
        ]
        middleLayer = [
                            Dot([150,150], self.canvas), Dot([250,150], self.canvas), Dot([350,150], self.canvas),
                            Dot([150,250], self.canvas),                                Dot([350,250], self.canvas),
                            Dot([150,350], self.canvas), Dot([250,350], self.canvas), Dot([350,350], self.canvas),
        ]
        outherLayer = [
                            Dot([100,100], self.canvas), Dot([250,100], self.canvas), Dot([400,100], self.canvas),
                            Dot([100,250], self.canvas),                                Dot([400,250], self.canvas),
                            Dot([100,400], self.canvas), Dot([250,400], self.canvas), Dot([400,400], self.canvas),
        ]

        gameMap = [innerLayer, middleLayer, outherLayer]

        for layer in range(len(gameMap)):
            for i in range(len(gameMap[layer])):
                nodes = []
                #if (i != 0 or i != 7 or i != 3 or i != 4):
                    #nodes.append(gameMap[layer][i-1])
                    #nodes.append(gameMap[layer][i+1])
                if (i == 0):
                    nodes.append(gameMap[layer][1])
                    nodes.append(gameMap[layer][3])
                elif (i == 3):
                    nodes.append(gameMap[layer][0])
                    nodes.append(gameMap[layer][5])
                    if (layer == 1):
                        nodes.append(gameMap[layer+1][3])
                        nodes.append(gameMap[layer-1][3])
                elif (i == 4):
                    nodes.append(gameMap[layer][2])
                    nodes.append(gameMap[layer][7])
                    if (layer == 1):
                        nodes.append(gameMap[layer+1][4])
                        nodes.append(gameMap[layer-1][4])
                elif (i == 7):
                    nodes.append(gameMap[layer][4])
                    nodes.append(gameMap[layer][6])
                elif (i == 2):
                    nodes.append(gameMap[layer][1])
                    nodes.append(gameMap[layer][4])
                elif (i == 5):
                    nodes.append(gameMap[layer][6])
                    nodes.append(gameMap[layer][3])
                else:
                    nodes.append(gameMap[layer][i+1])
                    nodes.append(gameMap[layer][i-1])
                    if (layer == 1):
                        if (i == 1):
                            nodes.append(gameMap[layer+1][1])
                            nodes.append(gameMap[layer-1][1])
                        elif (i == 6):
                            nodes.append(gameMap[layer+1][6])
                            nodes.append(gameMap[layer-1][6])
                gameMap[layer][i].setNext(nodes)

        self.canvas.pack()
        self.root.mainloop()

    def mainText(self, txt = None):
        if txt == None:
            txt = "Next move: "+self.nexdtMove
        self.gameText = Label(self.root, text=txt)
        self.gameText.pack()