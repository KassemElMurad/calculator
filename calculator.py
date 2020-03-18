from __future__ import division
from Tkinter import*

def onclk(num):
	global operator
	operator =operator + str(num)
	txtin.set(operator)

def clear():
	global operator
	operator=""
	txtin.set("")

def equ():
	global operator
	sum=str(eval(operator))
	txtin.set(sum)
	operator= sum

cal = Tk()
cal.title("calculator")
operator = ""
txtin = StringVar()
txtdis = Entry(cal,font=('arial', 20, 'bold'), textvariable=txtin, bd=30,insertwidth=4,bg="powder blue",justify='right').grid(columnspan=4)

btn7 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:onclk(7)).grid(row=1,column=0)
btn8 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:onclk(8)).grid(row=1,column=1)
btn9 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:onclk(9)).grid(row=1,column=2)
add = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:onclk("+")).grid(row=1,column=3)


btn4 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:onclk(4)).grid(row=2,column=0)
btn5 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:onclk(5)).grid(row=2,column=1)
btn6 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:onclk(6)).grid(row=2,column=2)
sub = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:onclk("-")).grid(row=2,column=3)


btn1 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:onclk(1)).grid(row=3,column=0)
btn2 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:onclk(2)).grid(row=3,column=1)
btn3 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:onclk(3)).grid(row=3,column=2)
mul = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:onclk("*")).grid(row=3,column=3)


btn0 = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:onclk(0)).grid(row=4,column=0)
deli = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="c",command=clear).grid(row=4,column=1)
eq = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="=",command=equ).grid(row=4,column=2)
ov = Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:onclk("/")).grid(row=4,column=3)
