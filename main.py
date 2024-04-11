from tkinter import *
from tkinter import ttk
import numexpr as ne
import sv_ttk


SIGNS = ["+", "-", "x", "÷"]
BGCOLOR = "#68838B"

def DisplayNumbers(num):
    """Exibe números na tela ao pressionar os botões numéricos."""
    screen.insert(END, num)

def DisplaySigns(char):
    """
    Exibe sinais de operação na tela ao pressionar os botões de operação.
    Verifica se já há um sinal de operação no final da expressão para evitar erros.
    Permite apenas a colocação do sinal de menos (-) no inicio para números negativos.
    """
    if len(screen.get()) == 0 and char == "-" :
        pass
    else:
        for sign in SIGNS:
            if sign in screen.get()[-1]:
                return None
    screen.insert(END, char)

def ClearScreen():
    """Limpa a tela da calculadora."""
    screen.delete(0, END)

def ClearLastEntry():
    """Remove o último caractere digitado na tela."""
    number_of_characters = len(screen.get())
    lastEntry = number_of_characters - 1
    screen.delete(lastEntry, END)

def GetResult():
    """Calcula o resultado da expressão na tela."""
    calculation = screen.get().replace("÷", "/").replace("x", "*")
    value = ne.evaluate(calculation)
    ClearScreen()
    return screen.insert(END, str(value))

# Janela
window = Tk()
window.title("Calculadora")
window.configure(background=BGCOLOR)
sv_ttk.set_theme("dark")

# Tela da calculadora
screen = Entry(window, width=20,font="arial")
screen.grid(column=0, row=0, columnspan=4, padx=30, pady=10, ipady=10)

# Botões numéricos
but1 = ttk.Button(window, text="1", width=3, command=lambda t=1: DisplayNumbers(t)).grid(column=0, row=2, pady=10)
but2 = ttk.Button(window, text="2", width=3, command=lambda t=2: DisplayNumbers(t)).grid(column=1, row=2)
but3 = ttk.Button(window, text="3", width=3, command=lambda t=3: DisplayNumbers(t)).grid(column=2, row=2)
but4 = ttk.Button(window, text="4", width=3, command=lambda t=4: DisplayNumbers(t)).grid(column=0, row=3, pady=7)
but5 = ttk.Button(window, text="5", width=3, command=lambda t=5: DisplayNumbers(t)).grid(column=1, row=3)
but6 = ttk.Button(window, text="6", width=3, command=lambda t=6: DisplayNumbers(t)).grid(column=2, row=3)
but7 = ttk.Button(window, text="7", width=3, command=lambda t=7: DisplayNumbers(t)).grid(column=0, row=4, pady=7)
but8 = ttk.Button(window, text="8", width=3, command=lambda t=8: DisplayNumbers(t)).grid(column=1, row=4)
but9 = ttk.Button(window, text="9", width=3, command=lambda t=9: DisplayNumbers(t)).grid(column=2, row=4)
but0 = ttk.Button(window, text="0", width=3, command=lambda t=0: DisplayNumbers(t)).grid(column=1, row=5, pady=7)

# Botões de operação
plusSign = ttk.Button(window, text="+", width=3, command=lambda t="+": DisplaySigns(t)).grid(column=3, row=2)
minusSign = ttk.Button(window, text="-", width=3, command=lambda t="-": DisplaySigns(t)).grid(column=3, row=3)
multiplicationSign = ttk.Button(window, text="x", width=3, command=lambda t="x": DisplaySigns(t)).grid(column=3, row=4)
divisionSign = ttk.Button(window, text="÷", width=3, command=lambda t="÷": DisplaySigns(t)).grid(column=3, row=5)

# Botões de resultado e limpeza
equalSign = ttk.Button(window, text="=", width=27, command=GetResult).grid(column=0, row=6, columnspan=4, pady=5)
clear = ttk.Button(window, text="C", width=11, command=ClearScreen).grid(column=0, row=1, columnspan=2)
clearEntry = ttk.Button(window, text="CE", width=11, command=ClearLastEntry).grid(column=2, row=1, columnspan=2)

window.mainloop()
