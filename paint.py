# A Very Basic Paint Applications in TKInter(You can draw a oval,Rectangle and freehand curves)
# Directions: Right-Click Twice at two points--Creates Rectangle
# Click: Creates a oval              
from tkinter import *
window = Tk()
def draw(event):
    #print(event.x,event.y)
    c.create_oval(event.x-1,event.y-1,event.x+1,event.y+1,fill="Red")
    # For different sizes change the 1s and play
def callback(event):
    c.create_oval(event.x-1,event.y-1,event.x+1,event.y+1,fill="Red")

def drawRectangle(event):
    global drawVar,x1,y1
    if drawVar:
        c.create_rectangle(x1,y1,event.x,event.y,fill="Blue")
        drawVar=False
    else:
        x1 = event.x
        y1 = event.y
        drawVar=True

c=Canvas(window,width=400,height=400)
c.pack()
c.bind("<Button-1>",callback)
c.bind("<B1-Motion>",draw)
c.bind("<Button-3>",drawRectangle)
drawVar=False
x1 = 0
y1 = 0
window.mainloop()