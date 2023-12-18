#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk
"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""

window = tk.Tk()
window.title("Your Birthdate")
window.attributes('-topmost',True)

def clickFunction(event):
    month2 = emonth.get()


    day2 = eday.get()


    year2 = eyear.get()



    answer = f"{month2}/{day2}/{year2}"
    entere.delete(0,END)
    entere.insert(3,answer)

EYB= tk.Label (window, text= "Enter your birthdate:")

month= tk.Label(window, text = "Month")
day= tk.Label (window, text= "Day")
year= tk.Label(window, text= "Year")

slash1= tk.Label (window, text= "/")
slash2= tk.Label(window, text= "/")

emonth = ttk.Combobox(window, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"],width=5)
eday = ttk.Spinbox(window, values=[ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 ],width=5)
eyear = ttk.Combobox(window, values= [1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937,1938,1939,1940,1941, 1942, 1943, 1944, 1945, 1946, 1947,1948,1949,1950,1951, 1952, 1953, 1954, 1955, 1956, 1957,1958,1959,1960,1961, 1962, 1963, 1964, 1965, 1966, 1967,1968,1969,1970,1971, 1972, 1973, 1974, 1975, 1976, 1977,1978,1979,1980,1981, 1982, 1983, 1984, 1985, 1986, 1987,1988,1989,1990,1991, 1992, 1993, 1994, 1995, 1996, 1997,1998,1999,2000,2001, 2002, 2003, 2004, 2005, 2006, 2007,2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,2018,2019,2020,2021, 2022, 2023,  ],width=5)

button = tk.Button(window, text= "Enter: ")
entere= tk.Entry(window, width= 10)
button.bind("<Button>",clickFunction)


EYB.grid(row = 1, column = 2, columnspan = 3)
month.grid(row = 2, column = 1 )
day.grid (row = 2, column = 3)
year. grid (row = 2, column = 5)

emonth.grid(row= 3, column= 1)
slash1.grid(row=3, column=2)
eday.grid (row= 3, column = 3)
slash2.grid(row=3, column=4)
eyear.grid (row =3, column = 5)

button.grid(row=4, column= 2)
entere.grid (row=4, column= 3)

window.mainloop()

