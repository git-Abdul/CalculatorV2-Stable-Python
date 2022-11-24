from tkinter import *
from dark_title_bar import *
screen = Tk()
screen.title('Calculator - Dev: Abdul Rehman')
screen.geometry("365x490")
screen.configure(bg='black')
screen.resizable(False, False)
screen.iconbitmap('icon.ico')
dark_title_bar(screen)


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
entry1 = Entry(screen,foreground='white' ,bg = '#212224',font =( 'airal',20,'italic bold'),bd='30', justify='right',textvariable=tex)
entry1.grid(row=0, columnspan=4)

#buttons
#row 1
btn7 = Button(screen,text='7', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),
              activebackground='#313334',activeforeground='white')
btn7.grid(row=1, column=0)

btn8 = Button(screen,text='8', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),
              activebackground='#313334',activeforeground='white')
btn8.grid(row=1, column=1)

btn9 = Button(screen,text='9', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),
              activebackground='#313334',activeforeground='white')
btn9.grid(row=1, column=2)

btnadd = Button(screen,text='+', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+'),
              activebackground='#313334',activeforeground='white')
btnadd.grid(row=1, column=3)
#row 2
btn4 = Button(screen,text='4', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),
              activebackground='#313334',activeforeground='white')
btn4.grid(row=2, column=0)

btn5 = Button(screen,text='5', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),
              activebackground='#313334',activeforeground='white')
btn5.grid(row=2, column=1)

btn6 = Button(screen,text='6', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),
              activebackground='#313334',activeforeground='white')
btn6.grid(row=2, column=2)

btnsub = Button(screen,text='-', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('-'),
              activebackground='#313334',activeforeground='white')
btnsub.grid(row=2, column=3)
#row3
btn1 = Button(screen,text='1', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),
              activebackground='#313334',activeforeground='white')
btn1.grid(row=3, column=0)

btn2 = Button(screen,text='2', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),
              activebackground='#313334',activeforeground='white')
btn2.grid(row=3, column=1)

btn3 = Button(screen,text='3', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),
              activebackground='#313334',activeforeground='white')
btn3.grid(row=3, column=2)

btnmulti = Button(screen,text='*', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('*'),
              activebackground='#313334',activeforeground='white')
btnmulti.grid(row=3, column=3)

#row 4
btn0 = Button(screen,text='0', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),
              activebackground='#313334',activeforeground='white')
btn0.grid(row=4, column=0)

btnclear = Button(screen,text='C', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground='#313334',activeforeground='white')
btnclear.grid(row=4, column=1)

btnequal = Button(screen,text='=', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground='#313334',activeforeground='white')
btnequal.grid(row=4, column=2)

btndiv = Button(screen,text='/', bg= '#212224',foreground='white',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('/'),
              activebackground='#313334',activeforeground='white')
btndiv.grid(row=4, column=3)

screen.mainloop()