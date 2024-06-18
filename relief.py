import tkinter as tk

def create_relief_demo():
    root = tk.Tk()
    root.title("Relief Types Demo")

    relief_types = ['flat', 'raised', 'sunken', 'groove', 'ridge']
    for idx, relief in enumerate(relief_types):
        frame = tk.Frame(root, relief=relief, bd=5)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        label = tk.Label(frame, text=relief, font=('Helvetica', 12))
        label.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_relief_demo()
