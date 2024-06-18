from tkinter import *


root= Tk()

def which_button(button_press):
    print(button_press)


b1=Button(root,text="APPLE",command=lambda m="it is an apple":which_button(m))
b1.grid(padx=10, pady=10)
b2= Button(root,text="orange",command=lambda m="it is an orange":which_button(m))
b2.grid(padx=10, pady=10)
root.mainloop()
