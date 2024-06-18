import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")
root.geometry("300x200")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="blue")

# Draw an oval
canvas.create_oval(50, 120, 150, 180, fill="red")

root.mainloop()
