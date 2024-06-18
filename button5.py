from tkinter import *


def changeonhover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e: button.config(background=colorOnLeave))
root=Tk()
mybutton=Button(root,text="on hover- Background change",bg="yellow")
mybutton.pack()

changeonhover(mybutton,"red","yellow")
root.mainloop()
    
