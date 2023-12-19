#!python3

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