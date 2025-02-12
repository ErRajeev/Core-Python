from tkinter import *
import tkinter as tk
root = tk.Tk()
root.title("calculator")
root.geometry('370x600')
root.configure(bg="black")

equation = ""


def show(value):
    global equation
    equation += value
    lbl_result.config(text=equation)


def clear():
    global equation
    equation = ""
    lbl_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = " Syntex Error"
            equation = ""
    lbl_result.config(text=result)


lbl_result = Label(root, width=25, height=2, text="", font=('arial', 30))
lbl_result.pack()

Button(root, text="C", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightblue', command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("/")).place(x=100, y=100)
Button(root, text="%", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("%")).place(x=190, y=100)
Button(root, text="X", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("*")).place(x=280, y=100)

Button(root, text="9", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightblue', command=lambda: show("9")).place(x=10, y=200)
Button(root, text="8", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("8")).place(x=100, y=200)
Button(root, text="7", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("7")).place(x=190, y=200)
Button(root, text="-", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("-")).place(x=280, y=200)

Button(root, text="6", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightblue', command=lambda: show("6")).place(x=10, y=300)
Button(root, text="5", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("5")).place(x=100, y=300)
Button(root, text="4", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("4")).place(x=190, y=300)
Button(root, text="+", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("+")).place(x=280, y=300)

Button(root, text="3", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightblue', command=lambda: show("3")).place(x=10, y=400)
Button(root, text="2", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("2")).place(x=100, y=400)
Button(root, text="1", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("1")).place(x=190, y=400)

Button(root, text="0", width=7, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show("0")).place(x=10, y=500)

Button(root, text=".", width=3, height=1, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='lightgreen', command=lambda: show(".")).place(x=190, y=500)
Button(root, text="=", width=3, height=3, font=("arial", 30, 'bold'), bd=1,
       fg='#fff', bg='#fe9037', command=lambda: calculate()).place(x=280, y=400)

root.mainloop()
