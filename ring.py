from tkinter import *

class Ring():
    def __init__(self, color, dot, gs):
        self.color = color
        self.gs = gs
        self.canvas = gs.canvas
        self.dot = dot
        self.ring = self.canvas.create_oval(self.dot.pos[0]-15,self.dot.pos[1]-15,self.dot.pos[0]+15,self.dot.pos[1]+15, fill=color)
        self.canvas.tag_bind(self.ring, '<1>', self.dot.on_click)
        pass