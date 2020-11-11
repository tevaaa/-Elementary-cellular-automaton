from tkinter import *
from cellular_automaton import*




def draw(liste):
    root = Tk()
    root.geometry("1920x1080")
    c = Canvas(root, height=1080, width=1920, bg="white")
    pos_x = 0
    pos_y = 0
    for j in range(len(liste)):
        for i in range(len(liste[j])):
            if liste[j][i] == 1:
                l = c.create_rectangle(pos_x, pos_y, pos_x+3, pos_y+3, fill = "black")
                c.pack()
            pos_x += 3
        pos_y += 3
        pos_x = 3
    root.mainloop()

draw(grille)


