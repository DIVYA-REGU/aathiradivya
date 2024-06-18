from tkinter import *
from tkinter.ttk import *

root=Tk()

root.geometry('400x500')

btn=Button(root,text ='click me',command= root.destroy)
btn.pack(side='top')

root.mainloop()
