from tkinter import *
from cellular_automaton import*
import time


gd = grid

root = Tk()
root.geometry("1200x800")
c = Canvas(root,width=1200, height=800,  bg="#FBFAF5")
pos_x = 0
pos_y = 0
for j in range(len(gd)-1):
    for i in range(len(gd)-1):
        if gd[j][i] == 1:
            l = c.create_rectangle(pos_x, pos_y, pos_x+3, pos_y+3, fill = "black")
        pos_x += 3
    c.pack()
    root.update()
    time.sleep(0.05)
    pos_y += 3
    pos_x = 3

