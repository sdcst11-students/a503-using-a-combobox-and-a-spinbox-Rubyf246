#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
window = tk.Tk()
window.title("tk!")
window.attributes('-topmost',True)

def clickFunction(event):
    #plus
    number1 = text1.get()
    number1=float(number1)
    number2 = text2.get()
    number2=float(number1)
    
    plus = operator.get()
    print (plus)
    if plus=="+":
        add= number1+number2
        answer = f"{add}"
        text3.delete(0,END)
        text3.insert(3,answer)
    else: 
        pass
    
    #subtract
    number1 = text1.get()
    number1=float(number1)
    number2 = text2.get()
    number2=float(number1)
    
    minus = operator.get()
    print (minus)
    if minus=="-":
        subtract= number1-number2
        answer = f"{subtract}"
        text3.delete(0,END)
        text3.insert(3,answer)
    else: 
        pass
    
     #times
    number1 = text1.get()
    number1=float(number1)
    number2 = text2.get()
    number2=float(number1)
    
    time = operator.get()
    print (time)
    if time=="x":
        multi= number1*number2
        answer = f"{multi}"
        text3.delete(0,END)
        text3.insert(3,answer)
    else: 
        pass
    
    #divide
    number1 = text1.get()
    number1=float(number1)
    number2 = text2.get()
    number2=float(number1)
    
    divide = operator.get()
    print (divide)
    if divide=="/":
        div= number1 / number2
        answer = f"{div}"
        text3.delete(0,END)
        text3.insert(3,answer)
    else: 
        pass

operator = ttk.Spinbox(values=["+", "-", "x", "/"],width=3)
equal = tk.Button(window,text="=")
text1= tk.Entry(window, width=10 )
text2 = tk.Entry (window, width = 10)
text3 = tk.Entry(window, width = 10 )
equal.bind("<Button>",clickFunction)

text1.grid(row = 1, column = 1)
text2.grid(row= 1, column =3 )
text3.grid(row=1, column=5)
operator.grid(row = 1, column = 2)
equal.grid(row = 1, column = 4)

window.mainloop()
