import tkinter as tk
import main

screenExpr = ""


def add(n):
    global screenExpr
    screenExpr += n
    label['text'] = screenExpr
    print(screenExpr)


def deleteLast():
    global screenExpr
    screenExpr = screenExpr[:-1]
    label['text'] = screenExpr


def execute():
    pass


def clear():
    global screenExpr
    screenExpr = ""
    label['text'] = screenExpr


def addOne():
    global screenExpr
    screenExpr += "1"
    label['text'] = screenExpr


def addTwo():
    global screenExpr
    screenExpr += "2"
    label['text'] = screenExpr


def addThree():
    global screenExpr
    screenExpr += "3"
    label['text'] = screenExpr


def addFour():
    global screenExpr
    screenExpr += "4"
    label['text'] = screenExpr


def addFive():
    global screenExpr
    screenExpr += "5"
    label['text'] = screenExpr


def addSix():
    global screenExpr
    screenExpr += "6"
    label['text'] = screenExpr


def addSeven():
    global screenExpr
    screenExpr += "7"
    label['text'] = screenExpr


def addEight():
    global screenExpr
    screenExpr += "8"
    label['text'] = screenExpr


def addNine():
    global screenExpr
    screenExpr += "9"
    label['text'] = screenExpr

# def add_sth():
#     global screenExpr
#     screenExpr +=


def addPoint():
    global screenExpr
    screenExpr += "."
    label['text'] = screenExpr


def addComma():
    global screenExpr
    screenExpr += ","
    label['text'] = screenExpr


def addPow():
    global screenExpr
    screenExpr += "^"
    label['text'] = screenExpr


def addSQ():
    global screenExpr
    screenExpr += "sq("
    label['text'] = screenExpr


def addZero():
    global screenExpr
    screenExpr += "0"
    label['text'] = screenExpr


def addPlus():
    global screenExpr
    screenExpr += "+"
    label['text'] = screenExpr


def addMinus():
    global screenExpr
    screenExpr += "-"
    label['text'] = screenExpr


def addMultiply():
    global screenExpr
    screenExpr += "*"
    label['text'] = screenExpr


def addDivide():
    global screenExpr
    screenExpr += "/"
    label['text'] = screenExpr


def addLB():
    global screenExpr
    screenExpr += "("
    label['text'] = screenExpr


def addRB():
    global screenExpr
    screenExpr += ")"
    label['text'] = screenExpr


def addSin():
    global screenExpr
    screenExpr += "sin("
    label['text'] = screenExpr


def addCos():
    global screenExpr
    screenExpr += "cos("
    label['text'] = screenExpr


def addTan():
    global screenExpr
    screenExpr += "tan("
    label['text'] = screenExpr


def addLn():
    global screenExpr
    screenExpr += "ln("
    label['text'] = screenExpr


def addLog():
    global screenExpr
    screenExpr += "log("
    label['text'] = screenExpr


root = tk.Tk()
root.title("Counting Seconds")
root.geometry("600x400+100+100")

label = tk.Label(root, text=screenExpr, width=60, height=2, background="WHITE", foreground="BLACK")
label.config(text=screenExpr)

one = tk.Button(root, text='1', width=2, height=2, command=addOne)
two = tk.Button(root, text='2', width=2, height=2, command=addTwo)
three = tk.Button(root, text='3', width=2, height=2, command=addThree)
four = tk.Button(root, text='4', width=2, height=2, command=addFour)
five = tk.Button(root, text='5', width=2, height=2, command=addFive)
six = tk.Button(root, text='6', width=2, height=2, command=addSix)
seven = tk.Button(root, text='7', width=2, height=2, command=addSeven)
eight = tk.Button(root, text='8', width=2, height=2, command=addEight)
nine = tk.Button(root, text='9', width=2, height=2, command=addNine)
zero = tk.Button(root, text='0', width=2, height=2, command=addZero)
plus = tk.Button(root, text='+', width=2, height=2, command=addPlus)
minus = tk.Button(root, text='-', width=2, height=2, command=addMinus)
multiply = tk.Button(root, text='*', width=2, height=2, command=addMultiply)
divide = tk.Button(root, text='/', width=2, height=2, command=addDivide)
pow = tk.Button(root, text='^', width=2, height=2, command=addPow)
comma = tk.Button(root, text=',', width=2, height=2, command=addComma)
point = tk.Button(root, text='.', width=2, height=2, command=addPoint)
l_b = tk.Button(root, text='(', width=2, height=2, command=addLB)
r_b = tk.Button(root, text=')', width=2, height=2, command=addRB)
sq = tk.Button(root, text='^', width=2, height=2, command=addSQ)
sin = tk.Button(root, text='sin', width=2, height=2, command=addSin)
cos = tk.Button(root, text='cos', width=2, height=2, command=addCos)
tan = tk.Button(root, text='tan', width=2, height=2, command=addTan)
ln = tk.Button(root, text='ln', width=2, height=2, command=addLn)
log = tk.Button(root, text='log', width=2, height=2, command=addLog)
equal = tk.Button(root, text='=', width=2, height=2, command=execute)
delete = tk.Button(root, text='<-', width=2, height=2, command=deleteLast)
clear = tk.Button(root, text='CE', width=2, height=2, command=clear)

label.grid(row=0, columnspan=7, pady=20)
one.grid(row=1, column=0, pady=10)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
l_b.grid(row=1, column=3)
r_b.grid(row=1, column=4)
sin.grid(row=1, column=5)
cos.grid(row=1, column=6)
four.grid(row=2, column=0, pady=10)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
plus.grid(row=2, column=3)
minus.grid(row=2, column=4)
tan.grid(row=2, column=5)
ln.grid(row=2, column=6)
seven.grid(row=3, column=0, pady=10)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
multiply.grid(row=3, column=3)
divide.grid(row=3, column=4)
log.grid(row=3, column=5)
delete.grid(row=3, column=6)
zero.grid(row=4, column=0, pady=10)
point.grid(row=4, column=1)
comma.grid(row=4, column=2)
sq.grid(row=4, column=3)
pow.grid(row=4, column=4)
equal.grid(row=4, column=5)
clear.grid(row=4, column=6)

root.mainloop()
