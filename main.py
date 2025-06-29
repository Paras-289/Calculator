
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar

app = tb.Window(themename="flatly")
app.title("Calculator")
app.geometry("230x300")

expression = ""

def click(val):
    global expression
    expression += val
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def equal():
    global expression
    try:
        expression = str(eval(expression))
        entry_var.set(expression)
    except:
        entry_var.set("Error")
        expression = ""

def back():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

entry_var = StringVar()
entry = tb.Entry(app, textvariable=entry_var, font=("Helvetica", 16), justify='right')
entry.pack(fill=X, padx=10, pady=10)

buttons = [
    ('C', '%', '*', 'x'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '-'),
    ('(', '0', ')', '=')
]

for row in buttons:
    frame = tb.Frame(app)
    frame.pack(pady=5)
    for char in row:
        if char == 'C':
            btn = tb.Button(frame, text=char, bootstyle="danger",width=3, command=clear)
        elif char == '=':
            btn = tb.Button(frame, text=char, bootstyle="success",width=3, command=equal)
        elif char == 'x':
            btn = tb.Button(frame, text="x", bootstyle="warning",width=3, command=back)
        else:
            btn = tb.Button(frame, text=char,width=3, command=lambda c=char: click(c))
        btn.pack(side=LEFT, padx=5)


app.mainloop()

