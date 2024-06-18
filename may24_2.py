import tkinter as tk
root=tk.Tk()
root.title("basic window")
root.geometry("1000x1000")
def on_button_click():
    label.config(text="button clicked")
def display_info():
    enteredtext=entry.get()
    label1.config(text=f"{enteredtext}")


label=tk.Label(root,text="hello tkinter!")
label.pack()
label1=tk.Label(root,text="hai divya")
label1.pack()

button=tk.Button(root,text="click on",command=on_button_click)
button.pack()

entry=tk.Entry()
entry.pack()

button=tk.Button(root,text="submit",command=display_info)
button.pack()



root.mainloop()
