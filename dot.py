class Dot():
    def __init__(self, pos, canvas, gs): # pos = [x,y], tonari = [ Dot args]
        self.pos = pos
        self.gs = gs
        self.dot = canvas.create_oval(pos[0]-10,pos[1]-10,pos[0]+10,pos[1]+10, fill="brown")
        self.canvas = canvas
        self.canvas.tag_bind(self.dot, '<1>', self.on_click)
        pass

    def setNext(self, tonari):
        self.tonari = tonari
        for i in tonari:
            if (i.pos != self.pos):
                self.canvas.create_line(self.pos[0], self.pos[1], i.pos[0], i.pos[1])
    
    def on_click(self, event):
        if (self.gs.gameState == 0):
            print("create ring")
        elif (self.gs.gameState == 1):
            for i in self.tonari:
                print("highlight: "+i)
        elif (self.gs.gameState == 2): # only 3 pices fron the right color WARNING
            for i in self.gs.gameMap:
                for l in i:
                    print("highlight: "+l)