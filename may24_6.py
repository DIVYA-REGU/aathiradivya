import tkinter as tk

def start_timer():
    global timer
    label.config(text=f"Timer: {timer}")
    timer += 1
    root.after(1000, start_timer)

root = tk.Tk()
root.title("Timer Example")
root.geometry("300x200")

timer = 0
label = tk.Label(root, text="Timer: 0")
label.pack(pady=20)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

root.mainloop()
