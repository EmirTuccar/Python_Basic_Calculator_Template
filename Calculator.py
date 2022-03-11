############################################
#
#   Basic Calculator
#
#    Emir Zekeriya Tüccar
#
##############################################






from tkinter import *


emir = Tk()
emir.title("Calculator")


emir.geometry("386x460")

e = Entry(emir,font="Comic 22 ", width= 20, borderwidth= 1, bg= "light blue", justify = RIGHT)
e.grid(row= 0, column= 0, columnspan= 5, padx= 30, pady= 0)

current = 0
current2 = 0

def button_click(number):
    eval = e.get()
    e.delete(0, END)
    e.insert(0, str(eval) + str(number))


def button_add():
    return
def button_clearE():
    e.delete(0, END)

def button_clear():
    e.delete(0, END)


def button_delete():
    current = e.get()
    global general
    general = int(len(current))
    e.delete(general - 1, general)
    general = int(current)



def button_plus():
    current = e.get()
    global general
    global operation
    operation = "plus"
    general = int(current)
    e.delete(0, END)

def button_minus():
    current = e.get()
    global general
    global operation
    operation = "minus"
    general = int(current)
    e.delete(0, END)

def button_multiply():
    current = e.get()
    global general
    global operation
    operation = "multiply"
    general = float(current)
    e.delete(0, END)

def button_divide():
    current = e.get()
    global general
    global operation
    operation = "divide"
    general = float(current)
    e.delete(0, END)

def button_negate():

    current = e.get()
    global general

    general = float(current)
    e.delete(0, END)
    grass = -1
    e.insert(0, general * grass)

def button_dividex():
    current = e.get()
    global general
    e.delete(0, END)

    general = float(current)
    tree = 1
    e.insert(0, tree / general)

def button_square():
    current = e.get()
    global general
    e.delete(0, END)
    general = float(current)
    plane = 2
    e.insert(0, general ** plane)

def button_square_root():
    current = e.get()
    global general
    e.delete(0, END)
    general = float(current)
    rock = 1/2
    e.insert(0, general ** rock)


def button_percent():
    current = e.get()
    global general
    e.delete(0, END)
    general = float(current)
    fire = 100
    e.insert(0, general / fire)


Mdigit = 0

def button_MPlus():
    mvalue = e.get()
    mvalue = float(mvalue)
    global Mdigit
    Mdigit = float(Mdigit)
    Mdigit = Mdigit + mvalue
    Mdigit = str(Mdigit)
    e.delete(0, END)


def button_MMinus():
    mvalue = e.get()
    mvalue = float(mvalue)
    global Mdigit
    Mdigit = float(Mdigit)
    Mdigit = Mdigit - mvalue
    Mdigit = str(Mdigit)
    e.delete(0, END)

def button_MS():
    global Mdigit
    a = e.get()
    Mdigit = float(a)

def button_MR():
    global Mdigit
    if float(Mdigit) == 0:
        e.delete(0, END)
        return
    e.delete(0, END)
    Mdigit = str(Mdigit)
    e.insert(0, Mdigit)


def button_MC():
    global Mdigit
    Mdigit = 0









def button_equal():
    current2 = e.get()

    e.delete(0, END)
    if operation == "plus" :
        e.insert(0, general + int(current2))
    elif operation == "minus" :
        e.insert(0, general - int(current2))
    elif operation == "multiply" :
        e.insert(0, general * int(current2))
    elif operation == "divide" :
        e.insert(0, general / int(current2))





button1 = Button(emir, text= "1", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(1))
button2 = Button(emir, text= "2", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(2))
button3 = Button(emir, text= "3", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(3))
button4 = Button(emir, text= "4", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(4))
button5 = Button(emir, text= "5", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(5))
button6 = Button(emir, text= "6", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(6))
button7 = Button(emir, text= "7", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(7))
button8 = Button(emir, text= "8", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(8))
button9 = Button(emir, text= "9", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(9))
button0 = Button(emir, text= "0", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_click(0))
buttonPlus = Button(emir, text= "+", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_plus())
buttonMinus = Button(emir, text= "-", padx= 42, pady=20,borderwidth=0,bg="light gray", command= lambda: button_minus())
buttonMultiply = Button(emir, text= "×", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_multiply())
buttonDivide = Button(emir, text= "÷", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_divide())
buttonComma = Button(emir, text= ",", padx= 42, pady=20,borderwidth=0,bg="light gray", command= lambda: button_clear())
buttonNegate = Button(emir, text= "+/-", padx= 34, pady=20,borderwidth=0,bg="light gray", command= lambda: button_negate())
buttonEqual = Button(emir, text= "=", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_equal())

buttonDivideX = Button(emir, text= "1/x", padx= 35, pady=20,borderwidth=0,bg="light gray", command= lambda: button_dividex())
buttonSquare = Button(emir, text= "x²", padx= 38, pady=20,borderwidth=0,bg="light gray", command= lambda: button_square())
buttonSquareRoot = Button(emir, text= "√x", padx= 36, pady=20,borderwidth=0,bg="light gray", command= lambda: button_square_root())
buttonPercent = Button(emir, text= "%", padx= 38, pady=20,borderwidth=0,bg="light gray", command= lambda: button_percent())
buttonCE = Button(emir, text= "CE", padx= 35, pady=20,borderwidth=0,bg="light gray", command= lambda: button_clearE())
buttonC = Button(emir, text= "C", padx= 40, pady=20,borderwidth=0,bg="light gray", command= lambda: button_clear())
buttonDelete = Button(emir, text= "⌫", padx= 37, pady=20,borderwidth=0,bg="light gray", command= lambda: button_delete())
buttonMC = Button(emir, text= "MC", padx= 25, pady=8,borderwidth=0,bg="light gray", command= lambda: button_MC())
buttonMR = Button(emir, text= "MR", padx= 25, pady=8,borderwidth=0,bg="light gray", command= lambda: button_MR())
buttonMPlus = Button(emir, text= "M+", padx= 25, pady=8,borderwidth=0,bg="light gray", command= lambda: button_MPlus())
buttonMMinus = Button(emir, text= "M-", padx= 25, pady=8,borderwidth=0,bg="light gray", command= lambda: button_MMinus())
buttonMS = Button(emir, text= "MS", padx=25, pady=8,borderwidth=0,bg="light gray", command= lambda: button_MS())


button1.place(x=0, y=333)
button2.place(x=99, y=333)
button3.place(x=195, y=333)
buttonPlus.place(x=292, y=333)

button4.place(x=0, y=269)
button5.place(x= 99, y=269)
button6.place(x=195, y=269)
buttonMinus.place(x=292, y=269)

button7.place(x=0, y=205)
button8.place(x=99 , y=205)
button9.place(x=195 , y=205)
buttonMultiply.place(x=292, y=205)

button0.place(x=99, y= 397)
buttonComma.place(x=195, y=397)
buttonNegate.place(x=0, y=397)
buttonEqual.place(x=292, y= 397)

buttonDivideX.place(x=0, y=141)
buttonSquare.place(x=99, y=141)
buttonSquareRoot.place(x=195, y=141)
buttonDivide.place(x=292, y=141)

buttonPercent.place(x=0, y=77)
buttonC.place(x=195, y=77)
buttonDelete.place(x=292, y=77)
buttonCE.place(x=99, y=77)

buttonMC.place(x=0,y=37)
buttonMR.place(x=80, y= 37)
buttonMPlus.place(x=158, y= 37)
buttonMMinus.place(x=236, y=37)
buttonMS.place(x=313,y=37)






emir.mainloop()
