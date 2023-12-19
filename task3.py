#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
window = tk.Tk()
window.title("Interest Calculator")
window.attributes('-topmost',True)

def clickFunction(event): 
    p = eprinciple.get()
    p=float(p)

    r = einterest.get()
    r=float(r)
    r=r/100
    
    n= ecompound.get()
    n=float(n)

    t= eyears.get()
    t=float(t)

    a = round(p * ((1+r/n)**(n*t)),2)
    answer=a
    ecalculate.delete(0,END)
    ecalculate.insert(3,answer)

begin= tk.Label(window, text= "Interest Calculator")

principle= tk.Label(window, text="Initial Investment =")
interest= tk.Label(window, text="Interest (%) =")
compound= tk.Label(window, text="Compounding Period in a year =")
years= tk.Label(window, text="Numbers of Years =")

eprinciple= tk.Entry(window, width=15)
einterest = tk.Entry (window, width = 15)
ecompound = ttk.Combobox(window, width = 10, value= [1,2,4,6,12,52,365] )
eyears = ttk.Combobox(window, width = 10, value = [1,2,3,4,5,6,7,8,9,10]  )

calculate=tk.Button(window, text= "Calculate")
ecalculate =tk.Entry(window, width=20)
calculate.bind("<Button>",clickFunction)

begin.grid(row= 1, column= 1, columnspan=2)

principle.grid(row=2, column=1)
interest.grid (row=3 , column = 1)
compound.grid(row=4, column=1)
years.grid (row =5, column = 1)

eprinciple.grid(row=2, column=2)
einterest.grid (row=3 , column = 2)
ecompound.grid(row=4, column=2)
eyears.grid (row =5, column = 2)

calculate.grid(row=7, column =1)
ecalculate.grid(row= 7, column=2)

window.mainloop()