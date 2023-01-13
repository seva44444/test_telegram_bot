import random
from tkinter import *
window = Tk()
window.title('Snake game')
HeightWindow = 800
WidthWindow = 800
IN_GAME = True
def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME = True
    canvas.delete(BLOCK)
    canvas.itemconfigure(restart_text,state='hidden')
    canvas.itemconfigure(game_over_text,state='hidden')
    start_game()
def start_game():
    global s
    create_apple()
    s = create_snake()
# Reaction on keypress
    canvas.bind("<KeyPress>", s.change_direction)
    main()

def set_state(item,state):
    canvas.itemconfigure(item,state=state)
def main():
    """ Handles game process """
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = canvas.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Check for collision with gamefield edges
        if x2 > WidthWindow or x1 < 0 or y1 < 0 or y2 > HeightWindow:
            IN_GAME = False
        # Eating apples
        elif head_coords == canvas.coords(BLOCK):
            s.add_segment()
            canvas.delete(BLOCK)
            create_apple()
    # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if head_coords == canvas.coords(s.segments[index].instance):
                    IN_GAME = False
        window.after(100, main)
    # Not IN_GAME -> stop game and print message
    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')
def create_snake():
    segments=[Segment(20,20),Segment(40,20),Segment(60,20)]
    return Snake(segments)
def create_apple():
    global BLOCK
    posx = 20 * random.randint(1,(WidthWindow-20)/20)
    posyx = 20 * random.randint(1,(HeightWindow-20)/20)
    BLOCK = canvas.create_oval(posx,posyx,posx+20,posyx+20,fill='red')
class Snake():
    def __init__(self,segments):
        self.segments=segments
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
    def move(self):
        """Moved the snake to the specified spector"""
        for index in range(0,len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = canvas.coords(self.segments[index + 1].instance)
            canvas.coords(segment, x1 ,y1,x2, y2)
        x1, y1, x2, y2 = canvas.coords(self.segments[-2].instance)

        canvas.coords(self.segments[-1].instance, x1 + self.vector[0] * 20, y1 + self.vector[1] * 20,
            x2 + self.vector[0] * 20, y2 + self.vector[1] * 20)
class Segment():
    def __init__(self, x,y):
        self.instance=canvas.create_rectangle(x,y , x+20,y+20,fill="green")
canvas = Canvas(window,height=800,width=800,bg='blue')
#segment=Segment(x=20,y=20)
game_over_text = canvas.create_text(WidthWindow / 2, HeightWindow / 2, text="GAME OVER!", font='Arial 20', fill='red', state='hidden')
restart_text = canvas.create_text(WidthWindow / 2, HeightWindow - HeightWindow / 3, font='Arial 30', fill='white', text="Click here to restart", state='hidden')
canvas.tag_bind(restart_text,"<Button-1>", clicked)
canvas.grid()
canvas.focus_set()
start_game()




window.mainloop()