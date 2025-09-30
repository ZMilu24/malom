class Dot():
    def __init__(self, pos, canvas): # pos = [x,y], next = [ Dot args]
        self.pos = pos
        self.dot = canvas.create_oval(pos[0]-10,pos[1]-10,pos[0]+10,pos[1]+10, fill="brown")
        pass

    def setNext(self, next):
        self.next = next
        for i in next:
            if (i.pos != self.pos):
                print("vonal rajzolás")
        