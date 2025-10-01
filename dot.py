class Dot():
    def __init__(self, pos, canvas): # pos = [x,y], tonari = [ Dot args]
        self.pos = pos
        self.dot = canvas.create_oval(pos[0]-10,pos[1]-10,pos[0]+10,pos[1]+10, fill="brown")
        self.canvas = canvas
        pass

    def setNext(self, tonari):
        self.tonari = tonari
        for i in tonari:
            if (i.pos != self.pos):
                self.canvas.create_line(self.pos[0], self.pos[1], i.pos[0], i.pos[1])
        