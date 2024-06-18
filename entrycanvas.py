from tkinter import *
from tkinter import messagebox

app=Tk()

def submit():
    messagebox.showinfo("submit","your information is successfully saved")


    entry1.delete(0,END)
    entry2.delete(0,END)

canvas_widget=Canvas(app,width="500",height="500")
canvas_widget.pack()

label1=Label(app,text="enter your name")
canvas_widget.create_window(150,160,window=label1)

label2=Label(app,text="enter password")
canvas_widget.create_window(150,200,window=label2)

entry1=Entry(app)
canvas_widget.create_window(300,160,window=entry1)

entry2=Entry(app)
canvas_widget.create_window(300,200,window=entry2)

button=Button(app,text="Submit",command=submit)
canvas_widget.create_window(220,250,window=button)

app.mainloop()


    
