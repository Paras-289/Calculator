from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Calculator")
root.geometry("215x230")
exp=""
def click(e):
    global exp
    
    exp=exp +e
    e1.insert(END,e)
def clear():
    global exp
    e1.delete(0,END)
    exp=""
def equal():
    global exp
    exp=str(eval(exp))
    print(exp)
    e1.delete(0,END)
    e1.insert(END,exp)
def back():
    global exp
    exp=exp[0:len(exp)-1]
    print(exp)
    e1.delete(0,END)
    e1.insert(END,exp)
    

e1=Entry(root,font=("Times New Roman",10,"bold"),width=26,bd=9,justify='right')
e1.place(x=0,y=0)
B1=Button(root,text="1",font=("Times New Roman",14),command=lambda:click('1'), width=2,bd=2)
B1.place(x=10,y=50)
B2=Button(root,text="2",font=("Times New Roman",14),command=lambda:click('2'), width=2,bd=2)
B2.place(x=50,y=50)
B3=Button(root,text="3",font=("Times New Roman",14),command=lambda:click('3'), width=2,bd=2)
B3.place(x=90,y=50)
B4=Button(root,text="C",font=("Times New Roman",14),command=clear, width=2,bd=2)
B4.place(x=130,y=50)
B5=Button(root,text="4",font=("Times New Roman",14),command=lambda:click('4'), width=2,bd=2)
B5.place(x=10,y=90)
B6=Button(root,text="5",font=("Times New Roman",14),command=lambda:click('5'), width=2,bd=2)
B6.place(x=50,y=90)
B7=Button(root,text="6",font=("Times New Roman",14),command=lambda:click('6'), width=2,bd=2)
B7.place(x=90,y=90)
B8=Button(root,text="+",font=("Times New Roman",14),command=lambda:click('+'), width=2,bd=2)
B8.place(x=170,y=90)
B9=Button(root,text="7",font=("Times New Roman",14),command=lambda:click('7'), width=2,bd=2)
B9.place(x=10,y=130)
B10=Button(root,text="8",font=("Times New Roman",14),command=lambda:click('8'), width=2,bd=2)
B10.place(x=50,y=130)
B11=Button(root,text="9",font=("Times New Roman",14),command=lambda:click('9'), width=2,bd=2)
B11.place(x=90,y=130)
B12=Button(root,text="- ",font=("Times New Roman",14),command=lambda:click('-'), width=2,bd=2)
B12.place(x=170,y=130)
B13=Button(root,text="*",font=("Times New Roman",14),command=lambda:click('*'), width=2,bd=2)
B13.place(x=130,y=90)
B14=Button(root,text="0",font=("Times New Roman",14),command=lambda:click('0'), width=2,bd=2)
B14.place(x=50,y=170)
B15=Button(root,text="/",font=("Times New Roman",14),command=lambda:click('/'), width=2,bd=2)
B15.place(x=130,y=130)
B16=Button(root,text="=",font=("Times New Roman",14),bg='#aecbe9',command=equal, width=2,bd=2)
B16.place(x=170,y=170)
B17=Button(root,text="X",font=("Times New Roman",14),command=back, width=2,bd=2)
B17.place(x=170,y=50)
B18=Button(root,text="(",font=("Times New Roman",14),command=lambda:click("("), width=2,bd=2)
B18.place(x=10,y=170)
B19=Button(root,text=")",font=("Times New Roman",14),command=lambda:click(")"), width=2,bd=2)
B19.place(x=90,y=170)
B20=Button(root,text="%",font=("Times New Roman",14),command=lambda:click("%"), width=2,bd=2)
B20.place(x=130,y=170)
root.mainloop()