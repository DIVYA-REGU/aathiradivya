from tkinter import *


root=Tk()

label1=Label(root,text="enter email-id : ")
label1.grid(row=0,column=0)

label2=Label(root,text="enter password : ")
label2.grid(row=1,column=0)

mystr=StringVar()
mystr.set('aadhiradivya@gmail.com')


entry1=Entry(textvariable=mystr,state=DISABLED).grid(row=0,column=1,padx=10,pady=10)
entry2=Entry().grid(row=1,column=1,padx=10,pady=10)
root.mainloop()
