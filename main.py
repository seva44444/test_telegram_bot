import random
from tkinter import *
window = Tk()
window.title('Snake game')
HeightWindow = 800
WidthWindow = 800
canvas = Canvas(window,height=800,width=800,bg='blue')
def create_snake():
    segments=[Segment(20,20),Segment(40,20),Segment(60,20)]
def create_apple():
    posx = 20 * random.randint(1,(WidthWindow-20)/20)
    posyx = 20 * random.randint(1,(HeightWindow-20)/20)
    BLOCK = canvas.create_oval(posx,posyx,posx+20,posyx+20,fill='red')
def change_direction(self,event):
    """Changes direction of snake"""
    if event.keysym in self.mapping:
        self.vector = self.mapping[event.keysym]

class Snake():
    def __init__(self,segments):
        self.segment=segments
        self.mapping = {"Down":(0,1),"Right":(1,0),"Up":(0,-1),"Left":(-1,0)}
        self.vector = self.mapping["Down"]
    def change_direction(self, event):
        """Changes direction of snake"""
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
    def reset_snake(self):
        for segment in self.segments:#1) создай переменную  segment[1,2,3,'[хи бро
            #2) клади в переменную сегмент все элементы списка сегментс
            canvas.delete(segment.instance)
    def add_segment(self):
        """Adds segment to the snake"""
        last_seg = canvas.coords(self.segments[0].instance)
        x = last_seg[2]- 20
        y = last_seg[3]- 20
        self.segments.insert(0,Segment(x,y))
class Segment():
    def __init__(self, x,y):
        self.instance=canvas.create_rectangle(x,y , x+20,y+20,fill="green")
segment=Segment(x=20,y=20)
canvas.grid()
canvas.focus_set()
create_apple()




window.mainloop()