from tkinter import *
from tkinter import ttk

SIGNS = ["+", "-", "x", "÷"]
BGCOLOR = "#68838B"
THEME = "default" # [""clam", "alt", "default", "classic"]

def DisplayNumbers(char):
    screen.insert(END, char)

def DisplaySigns(char):
    for sign in SIGNS:
        if sign in screen.get()[-1]:
            return None
    screen.insert(100, char)

def ClearScreen():
    screen.delete(0, END)

def ClearLastEntry():
    number_of_characters = len(screen.get())
    lastEntry = number_of_characters - 1
    screen.delete(lastEntry, END)

def GetResult():
    for sign in SIGNS:
        if sign in screen.get():
            calculation = screen.get()
            try:
                value = eval(calculation)
                ClearScreen()
                return screen.insert(END, str(value))
            except SyntaxError:
                if sign == "÷":
                    calcRep = calculation.replace("÷", "/")
                    value = eval(calcRep)
                if sign == "x":
                    calcRep = calculation.replace("x", "*")
                    value = eval(calcRep)
                ClearScreen()
                return screen.insert(END, str(value))
            
            
window = Tk()
window.title("Calculadora")
window.configure(background=BGCOLOR)
ttk.Style().theme_use(THEME)

screen = Entry(window, width=30)
screen.grid(column=0, row=0, columnspan=4, padx=30, pady=10, ipady=10)

but1 = ttk.Button(window, text="1", width=5, command=lambda t=1: DisplayNumbers(t)).grid(column=0, row=2, pady= 10)
but2 = ttk.Button(window, text="2", width=5, command=lambda t=2: DisplayNumbers(t)).grid(column=1, row=2)
but3 = ttk.Button(window, text="3", width=5, command=lambda t=3: DisplayNumbers(t)).grid(column=2, row=2)

but4 = ttk.Button(window, text="4", width=5, command=lambda t=4: DisplayNumbers(t)).grid(column=0, row=3, pady= 7)
but5 = ttk.Button(window, text="5", width=5, command=lambda t=5: DisplayNumbers(t)).grid(column=1, row=3)
but6 = ttk.Button(window, text="6", width=5, command=lambda t=6: DisplayNumbers(t)).grid(column=2, row=3)

but7 = ttk.Button(window, text="7", width=5, command=lambda t=7: DisplayNumbers(t)).grid(column=0, row=4, pady= 7)
but8 = ttk.Button(window, text="8", width=5, command=lambda t=8: DisplayNumbers(t)).grid(column=1, row=4)
but9 = ttk.Button(window, text="9", width=5, command=lambda t=9: DisplayNumbers(t)).grid(column=2, row=4)

but0 = ttk.Button(window, text="0", width=5, command=lambda t=0: DisplayNumbers(t)).grid(column=1, row=5, pady= 7)

plusSign = ttk.Button(window, text="+", width=5, command=lambda t="+": DisplaySigns(t)).grid(column=3, row=2)
minusSign = ttk.Button(window, text="-", width=5, command=lambda t="-": DisplaySigns(t)).grid(column=3, row=3)
multiplicationSign = ttk.Button(window, text="x", width=5, command=lambda t="x": DisplaySigns(t)).grid(column=3, row=4)
divisionSign = ttk.Button(window, text="÷", width=5, command=lambda t="÷": DisplaySigns(t)).grid(column=3, row=5)

equalSign = ttk.Button(window, text="=", width=35, command=GetResult).grid(column=0, row=6, columnspan=4, pady=5)
clear = ttk.Button(window, text="C", width=15, command=ClearScreen).grid(column=0, row=1, columnspan=2)
clearEntry = ttk.Button(window, text="CE", width=15, command=ClearLastEntry).grid(column=2, row=1, columnspan=2)


window.mainloop()
