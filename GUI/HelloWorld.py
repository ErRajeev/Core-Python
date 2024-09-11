from tkinter import *
root = Tk()


def onClick():
    pass

root.title('Len Den Bamk')
root.geometry('480x620')
lbl = Label(root, text="Hello ")
lbl.grid(column=0, row=0)
txt = Entry(root, width=30)
txt.grid(column=1, row=1)
btn = Button(root, text="Enter", fg='red', bg='yellow', command=onClick())
btn.grid(column=10, row=1)
root.mainloop()

