from tkinter import *

top = Tk()


def correct(v, inp):
    if inp.isdigit():
        print(v)
        return True
    elif inp is "":
        print(inp)
        return True
    else:
        print(inp)
        return False


e = Entry(top)
e.place(x=50, y=50)
reg = top.register(correct)
e.config(validate="key", validatecommand=(reg, '%v', '%P'))
top.mainloop()
