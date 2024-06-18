import tkinter as tk

# Creating the root window
root = tk.Tk()

# Creating the Label with the text 'Middle'
Label_middle = tk.Label(root, text='Middle')

# Placing the Label at the middle of the root window without anchor
Label_middle.place(relx=0.5, rely=0.5,anchor='nw')

# Execute Tkinter
root.mainloop()
