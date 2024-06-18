import tkinter as tk

root=tk.Tk()
root.geometry("400x500")
root.title("entry example")

name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=passw_var.get()

    print("name is:" + name)
    print("password is:" + password)

    name_var.set("")
    passw_var.set("")


label1=tk.Label(root,text="ENTER USERNAME:")
entry1=tk.Entry(root,textvariable=name_var)
label2=tk.Label(root,text="ENTER PASSWORD:")
entry2=tk.Entry(root,textvariable=passw_var)
button=tk.Button(root,text="Submit",command=submit)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
button.grid(row=2,column=1)


root.mainloop()
