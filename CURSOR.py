from tkinter import *

app=Tk()


def shift_left(event=None):
    position=entrylabel.index(INSERT)
    entrylabel.icursor(position - 1)

def shift_right(event=None):
    position=entrylabel.index(INSERT)
    entrylabel.icursor(position + 1)


button1=Button(app,text="shift cursor left",command=shift_left)
button1.grid(row=2,column=3,padx=10,pady=10)

button2=Button(app,text="shift cursor right",command=shift_right)
button2.grid(row=2,column=9,padx=10,pady=10)

entrylabel=Entry(app)
entrylabel.grid(row=0,column=6,padx=10,pady=10)

entrylabel.focus

app.mainloop()
