from tkinter import *

root=Tk()
root.title("button border")
root.geometry("400x450")
l=Label(root,text="enter the name",font=("Times New Roman",17))
l.pack(pady=(5,10))
entry=Entry(root,text=" ")
entry.pack(pady =(5,10))
border=Frame(root,bd="6",bg="Black")
border.pack(pady =(5,10))
button=Button(border,text="submit",bg="white",activebackground="orange",borderwidth="0")
button.pack(pady =(5,10))


root.mainloop()
           
    
