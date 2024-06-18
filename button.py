import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("basic window")

def show_message():
    messagebox.showinfo("information,this is a message")

button=tk.Button(root,text="show message",command=show_message)
button.pack()

root.mainloop()
l
