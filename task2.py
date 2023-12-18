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



operator = ttk.Spinbox(values=["+", "-", "x", "/"],width=3)
equal = tk.Label(window,text="=")
text1= tk.Entry(window, width=10 )
text2 = tk.Entry (window, width = 10)
text3 = tk.Entry(window, width = 10 )

text1.grid(row = 1, column = 1)
text2.grid(row= 1, column =3 )
text3.grid(row=1, column=5)
operator.grid(row = 1, column = 2)
equal.grid(row = 1, column = 4)





window.mainloop()
