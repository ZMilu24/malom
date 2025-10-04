class Dot():
    def __init__(self, pos, canvas, gs): # pos = [x,y], tonari = [ Dot args]
        self.pos = pos
        self.gs = gs
        self.canvas = canvas
        self.highlight = None
        self.ringColor = None
        self.getClicked = False
        self.CreateDot()

    def CreateDot(self):
        self.dot = self.canvas.create_oval(self.pos[0]-20,self.pos[1]-20,self.pos[0]+20,self.pos[1]+20, fill="black")
        self.canvas.tag_bind(self.dot, '<1>', self.on_click)

    def setNext(self, tonari):
        self.tonari = tonari
        for i in tonari:
            if (i.pos != self.pos):
                self.canvas.create_line(self.pos[0], self.pos[1], i.pos[0], i.pos[1])
    
    def Highlight(self):
        self.highlight = self.canvas.create_oval(self.pos[0]-25,self.pos[1]-25,self.pos[0]+25,self.pos[1]+25, fill="red")
        self.CreateDot()

    def HighlightTonari(self):
        for i in self.gs.gameMap:
            for l in i:
                if (l.highlight != None):
                    l.DeleteHighlight()
        for i in self.tonari:
            i.Highlight()

    def DeleteHighlight(self):
        self.canvas.delete(self.highlight)

    def on_click(self, event):
        print("get clicked")
        for i in self.gs.gameMap:
            for l in i:
                l.getClicked = False
        self.getClicked = True
        self.gs.buttonGetClicked(self)

        '''
        if (self.highlight == None):
            self.HighlightTonari()
        else:
            print("move")
        if (self.gs.gameState == 0):
            print("create ring")
        elif (self.gs.gameState == 1):
            for i in self.tonari:
                i.Highlight()
        elif (self.gs.gameState == 2): # only 3 pices fron the right color WARNING
            for i in self.gs.gameMap:
                for l in i:
                    if l != self:
                        print("highlight: "+l)
        '''