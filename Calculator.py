from tkinter import *
screen = Tk()
screen.title('Calculator - Dev: Abdul Rehman')
screen.geometry("365x490")
screen.configure(bg='black')
screen.resizable(False, False)

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator = str(result)
    tex.set(result)

tex = StringVar()
operator = ''

#typer
entry1 = Entry(screen,bg = 'orange',font =( 'airal',20,'italic bold'),bd='30', justify='right',textvariable=tex)
entry1.grid(row=0, columnspan=4)

#buttons
#row 1
btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),
              activebackground='red',activeforeground='green')
btn7.grid(row=1, column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),
              activebackground='red',activeforeground='green')
btn8.grid(row=1, column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),
              activebackground='red',activeforeground='green')
btn9.grid(row=1, column=2)

btnadd = Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),
              activebackground='red',activeforeground='green')
btnadd.grid(row=1, column=3)
#row 2
btn4 = Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),
              activebackground='red',activeforeground='green')
btn4.grid(row=2, column=0)

btn5 = Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),
              activebackground='red',activeforeground='green')
btn5.grid(row=2, column=1)

btn6 = Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),
              activebackground='red',activeforeground='green')
btn6.grid(row=2, column=2)

btnsub = Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('-'),
              activebackground='red',activeforeground='green')
btnsub.grid(row=2, column=3)
#row3
btn1 = Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),
              activebackground='red',activeforeground='green')
btn1.grid(row=3, column=0)

btn2 = Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),
              activebackground='red',activeforeground='green')
btn2.grid(row=3, column=1)

btn3 = Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),
              activebackground='red',activeforeground='green')
btn3.grid(row=3, column=2)

btnmulti = Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('*'),
              activebackground='red',activeforeground='green')
btnmulti.grid(row=3, column=3)

#row 4
btn0 = Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),
              activebackground='red',activeforeground='green')
btn0.grid(row=4, column=0)

btnclear = Button(screen,text='C',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground='red',activeforeground='green')
btnclear.grid(row=4, column=1)

btnequal = Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground='red',activeforeground='green')
btnequal.grid(row=4, column=2)

btndiv = Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),
              activebackground='red',activeforeground='green')
btndiv.grid(row=4, column=3)

screen.mainloop()