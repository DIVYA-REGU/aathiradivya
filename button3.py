from tkinter import *
import random

root=Tk()
root.title("button")
root.geometry("400x400")

btn=Button(root,text="click me!")
btn.pack()

def clicked(event):
    x=random.randint(50,200)
    y=random.randint(50,250)
    btn.place(x=x,y=y)

btn.bind("<Button-1>",clicked)
btn.pack()

root.mainloop()
