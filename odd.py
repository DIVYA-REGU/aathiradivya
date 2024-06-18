import tkinter as tk

root=tk.Tk()
root.title("find odd or even")

def submit():
    entry1=entry.get()
    try:
        number=int(entry1)
        if number%2==0:
            result_label.config(text=f"{number} is even")
        else:
            result_label.config(text=f"{number} is odd")
    except ValueError:
        result_label.config(text="please enter a valid number")
    


label=tk.Label(root,text="enter the number:")
label.pack()
entry=tk.Entry(root)
entry.pack()
sub_btn=tk.Button(root,text='submit',command=submit)
sub_btn.pack()
result_label=tk.Label(root,text="")
result_label.pack()


root.mainloop()
                  
