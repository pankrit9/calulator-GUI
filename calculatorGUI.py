
def Click(btn):
    exp = strVar.get()
    if btn == '=':
        exp = eval(exp)
    elif btn == 'c':
        exp = ''
    else:
        if exp == '0':
            exp = btn
        else:
            exp += btn
    strVar.set(exp)

import tkinter as tk

window = tk.Tk()

strVar = tk.StringVar()
strVar.set('')

tk.Label(window, textvariable = strVar).grid(row = 0, column = 0, columnspan = 3)

tk.Button(window, text = 'c', width = 5, height = 2, command = lambda : Click('c')).grid(row = 0, column = 3)

tk.Button(window, text = '7', width = 5, height = 2, command = lambda : Click('7')).grid(row = 1, column = 0)
tk.Button(window, text = '8', width = 5, height = 2, command = lambda : Click('8')).grid(row = 1, column = 1)
tk.Button(window, text = '9', width = 5, height = 2, command = lambda : Click('9')).grid(row = 1, column = 2)
tk.Button(window, text = '/', width = 5, height = 2, command = lambda : Click('/')).grid(row = 1, column = 3)

tk.Button(window, text = '4', width = 5, height = 2, command = lambda : Click('4')).grid(row = 2, column = 0)
tk.Button(window, text = '5', width = 5, height = 2, command = lambda : Click('5')).grid(row = 2, column = 1)
tk.Button(window, text = '6', width = 5, height = 2, command = lambda : Click('6')).grid(row = 2, column = 2)
tk.Button(window, text = '*', width = 5, height = 2, command = lambda : Click('*')).grid(row = 2, column = 3)

tk.Button(window, text = '1', width = 5, height = 2, command = lambda : Click('1')).grid(row = 3, column = 0)
tk.Button(window, text = '2', width = 5, height = 2, command = lambda : Click('2')).grid(row = 3, column = 1)
tk.Button(window, text = '3', width = 5, height = 2, command = lambda : Click('3')).grid(row = 3, column = 2)
tk.Button(window, text = '-', width = 5, height = 2, command = lambda : Click('-')).grid(row = 3, column = 3)

tk.Button(window, text = '.', width = 5, height = 2, command = lambda : Click('.')).grid(row = 4, column = 0)
tk.Button(window, text = '0', width = 5, height = 2, command = lambda : Click('0')).grid(row = 4, column = 1)
tk.Button(window, text = '=', width = 5, height = 2, command = lambda : Click('=')).grid(row = 4, column = 2)
tk.Button(window, text = '+', width = 5, height = 2, command = lambda : Click('+')).grid(row = 4, column = 3)

window.title('Calulator')

window.mainloop()