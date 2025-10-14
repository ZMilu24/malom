from tkinter import *
from dot import Dot
from ring import Ring

class GameScreen():
    def __init__(self, winsize = 800):

        # global game variables
        self.gameState = 0  # 0 - start ; 1 - middle game ; 2 - endgame ; 3 - winner screen
        self.nexdtMove = "white"

        self.winner = None
        self.gameText = None
        self.selectedDot = None

        self.whiteRingsOnMap = 0
        self.blackRingsOnMap = 0

        self.whiteRingsOffMap = 9
        self.blackRingsOffMap = 9

        self.whiteRings =   []
        self.blackRings =   []
        self.ThreeMan =     []

        self.mansGame = False

        #create game map
        self.root = Tk()
        self.root.minsize(winsize,winsize)
        self.root.maxsize(winsize,winsize)
        self.root.geometry(str(winsize)+"x"+str(winsize))
        self.canvas = Canvas(self.root, width=winsize, height=winsize, bg="#101b3d")

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
                    elif (layer == 0):
                        nodes.append(self.gameMap[layer+1][3])
                    else:
                        nodes.append(self.gameMap[layer-1][3])
                elif (i == 4):
                    nodes.append(self.gameMap[layer][2])
                    nodes.append(self.gameMap[layer][7])
                    if (layer == 1):
                        nodes.append(self.gameMap[layer+1][4])
                        nodes.append(self.gameMap[layer-1][4])
                    elif (layer == 0):
                        nodes.append(self.gameMap[layer+1][4])
                    else:
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
                    elif (layer == 0):
                        if (i == 1):
                            nodes.append(self.gameMap[layer+1][1])
                        elif (i == 6):
                            nodes.append(self.gameMap[layer+1][6])
                    elif (layer == 2):
                        if (i == 1):
                            nodes.append(self.gameMap[layer-1][1])
                        elif (i == 6):
                            nodes.append(self.gameMap[layer-1][6])
                self.gameMap[layer][i].setNext(nodes)

        for layer in self.gameMap:
            for i in layer:
                i.Highlight()
                i.DeleteHighlight()

        self.canvas.pack()

        self.root.mainloop()

    def stateHandler(self):
        if self.whiteRingsOffMap == 0 and self.blackRingsOffMap == 0:
            self.gameState = 1

    def shutDownHighlight(self):
        print("shut down highlight")
        for layer in self.gameMap:
            for i in layer:
                i.DeleteHighlight()

    def createRing(self, dot):
        ring = Ring(self.nexdtMove, dot, self)
        dot.ring = ring
        return(ring)
    
    def WhiteGame(self, lista, dot):
        if dot.ring in lista:
            self.mansGame = True
            self.ThreeMan.append(lista)
            for layer in self.gameMap:
                for i in layer:
                    if i.ring != None:
                        if i.ring.color == "black":
                            flag = True
                            for l in self.ThreeMan:
                                if i.ring in l:
                                    flag = False
                            if flag:
                                i.Highlight()
            
    def BlackGame(self, lista, dot):
        if dot.ring in lista:
            self.mansGame = True
            self.ThreeMan.append(lista)
            for layer in self.gameMap:
                for i in layer:
                    if i.ring != None:
                        if i.ring.color == "white":
                            flag = True
                            for l in self.ThreeMan:
                                if i.ring in l:
                                    flag = False
                            if flag:
                                i.Highlight()

    def ThreeMansGame(self, dot):
        for layer in range(len(self.gameMap)):
            #White
            try:
                if self.gameMap[layer][0].ring.color == "white" and self.gameMap[layer][1].ring.color == "white" and self.gameMap[layer][2].ring.color == "white":
                    self.WhiteGame([self.gameMap[layer][0].ring, self.gameMap[layer][1].ring, self.gameMap[layer][2].ring], dot)
            except:
                print()
            try:
                if self.gameMap[layer][5].ring.color == "white" and self.gameMap[layer][6].ring.color == "white" and self.gameMap[layer][7].ring.color == "white":
                    self.WhiteGame([self.gameMap[layer][5].ring, self.gameMap[layer][6].ring, self.gameMap[layer][7].ring], dot)
            except:
                print()

            try:
                if self.gameMap[layer][2].ring.color == "white" and self.gameMap[layer][4].ring.color == "white" and self.gameMap[layer][7].ring.color == "white":
                    self.WhiteGame([self.gameMap[layer][2].ring, self.gameMap[layer][4].ring, self.gameMap[layer][7].ring], dot)
            except:
                print()

            try:
                if self.gameMap[layer][0].ring.color == "white" and self.gameMap[layer][3].ring.color == "white" and self.gameMap[layer][5].ring.color == "white":
                    self.WhiteGame([self.gameMap[layer][0].ring, self.gameMap[layer][3].ring, self.gameMap[layer][5].ring], dot)
            except:
                print()

            #Balck
            try:
                if self.gameMap[layer][0].ring.color == "black" and self.gameMap[layer][1].ring.color == "black" and self.gameMap[layer][2].ring.color == "black":
                    self.BlackGame([self.gameMap[layer][0].ring, self.gameMap[layer][1].ring, self.gameMap[layer][2].ring], dot)
            except:
                print()

            try:
                if self.gameMap[layer][5].ring.color == "black" and self.gameMap[layer][6].ring.color == "black" and self.gameMap[layer][7].ring.color == "black":
                    self.BlackGame([self.gameMap[layer][5].ring, self.gameMap[layer][6].ring, self.gameMap[layer][7].ring], dot)
            except:
                print()

            try:
                if self.gameMap[layer][2].ring.color == "black" and self.gameMap[layer][4].ring.color == "black" and self.gameMap[layer][7].ring.color == "black":
                    self.BlackGame([self.gameMap[layer][2].ring, self.gameMap[layer][4].ring, self.gameMap[layer][7].ring], dot)
            except:
                print()

            try:
                if self.gameMap[layer][0].ring.color == "black" and self.gameMap[layer][3].ring.color == "black" and self.gameMap[layer][5].ring.color == "black":
                    self.BlackGame([self.gameMap[layer][0].ring, self.gameMap[layer][3].ring, self.gameMap[layer][5].ring], dot)
            except:
                print()

        
        #White
        try:
            if self.gameMap[0][1].ring.color == "white" and self.gameMap[1][1].ring.color == "white" and self.gameMap[2][1].ring.color == "white":
                self.WhiteGame([self.gameMap[0][1].ring, self.gameMap[1][1].ring, self.gameMap[2][1].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][3].ring.color == "white" and self.gameMap[1][3].ring.color == "white" and self.gameMap[2][3].ring.color == "white":
                self.WhiteGame([self.gameMap[0][3].ring, self.gameMap[1][3].ring, self.gameMap[2][3].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][4].ring.color == "white" and self.gameMap[1][4].ring.color == "white" and self.gameMap[2][4].ring.color == "white":
                self.WhiteGame([self.gameMap[0][4].ring, self.gameMap[1][4].ring, self.gameMap[2][4].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][6].ring.color == "white" and self.gameMap[1][6].ring.color == "white" and self.gameMap[2][6].ring.color == "white":
                self.WhiteGame([self.gameMap[0][6].ring, self.gameMap[1][6].ring, self.gameMap[2][6].ring], dot)
        except:
            print()

            
        #White
        try:
            if self.gameMap[0][1].ring.color == "black" and self.gameMap[1][1].ring.color == "black" and self.gameMap[2][1].ring.color == "black":
                self.BlackGame([self.gameMap[0][1].ring, self.gameMap[1][1].ring, self.gameMap[2][1].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][3].ring.color == "black" and self.gameMap[1][3].ring.color == "black" and self.gameMap[2][3].ring.color == "black":
                self.BlackGame([self.gameMap[0][3].ring, self.gameMap[1][3].ring, self.gameMap[2][3].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][4].ring.color == "black" and self.gameMap[1][4].ring.color == "black" and self.gameMap[2][4].ring.color == "black":
                self.BlackGame([self.gameMap[0][4].ring, self.gameMap[1][4].ring, self.gameMap[2][4].ring], dot)
        except:
            print()

        try:
            if self.gameMap[0][6].ring.color == "black" and self.gameMap[1][6].ring.color == "black" and self.gameMap[2][6].ring.color == "black":
                self.BlackGame([self.gameMap[0][6].ring, self.gameMap[1][6].ring, self.gameMap[2][6].ring], dot)
        except:
            print()

    def buttonGetClicked(self, dot):

        def onMapRemover():
            if (dot.ring.color == "white"):
                self.whiteRingsOnMap -= 1
            else:
                self.blackRingsOnMap -= 1

        def ColorChange():
            print("color change")
            if self.selectedDot == None:
                if self.nexdtMove == "white":
                    self.nexdtMove = "black"
                else:
                    self.nexdtMove = "white"

        def RingRemover():
            if dot.highlight != None:
                print("KILL")
                if dot.ring != None:
                    onMapRemover()
                dot.DeleteRing()
                self.shutDownHighlight()
                self.mansGame = False

        # cer 1:
        if self.gameState == 0:
            if (self.mansGame == False):
                if dot.ring == None:
                    if self.nexdtMove == "white" and self.whiteRingsOffMap > 0:
                        ring = self.createRing(dot)
                        self.whiteRings.append(ring)
                        self.whiteRingsOffMap -= 1
                        self.whiteRingsOnMap += 1
                    elif self.nexdtMove == "black" and self.blackRingsOffMap > 0:
                        ring = self.createRing(dot)
                        self.blackRings.append(ring)
                        self.blackRingsOffMap -= 1
                        self.blackRingsOnMap += 1
                    ColorChange()
            else:
                if dot.ring != None:
                    onMapRemover()
                RingRemover()
        # cer 2:
        elif self.gameState == 1:
            if dot.highlight != None:
                if (self.mansGame == False):
                    #create new ring + delete old ring
                    ring = self.createRing(dot)
                    if self.nexdtMove == "white":
                        self.whiteRings.append(ring)
                        self.whiteRings.remove(self.selectedDot.ring)
                    elif self.nexdtMove == "black":
                        self.blackRings.append(ring)
                        self.blackRings.remove(self.selectedDot.ring)
                    dot.DeleteHighlight()
                    self.selectedDot.DeleteRing()
                    self.selectedDot = None
                    self.shutDownHighlight()
                    if self.mansGame == False:
                        ColorChange()
                else:
                    RingRemover()
            elif dot.ring != None:
                if dot.ring.color == self.nexdtMove:
                    dot.HighlightTonari()
                    self.selectedDot = dot
        try:
            if dot.ring != None:
                if self.gameState == 0:
                    self.ThreeMansGame(dot)
                else:
                    if self.selectedDot == None:
                        self.ThreeMansGame(dot)
                if self.mansGame == True:
                    if dot.ring.color != self.nexdtMove:
                        RingRemover()
        except:
            print()
        self.stateHandler()
        print(self.nexdtMove)