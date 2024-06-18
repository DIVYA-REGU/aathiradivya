from tkinter import *


def lang_update(language):
    text.delete(0,END)
    text.insert(0,language)


root=Tk()
root.title("button")
root.geometry("400x400")

text=Entry(root,bg="white")
text.pack()

button_dict={}
word=['python','javascript','c']
for lang in word:
    def action(x=lang):
        return lang_update(x)
    button_dict[lang]=Button(root,text=lang,command=action)
    button_dict[lang].pack()
root.mainloop()
