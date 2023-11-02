from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = str(first.get())
        final.set(eval(value))
        ttk.Label(text=f'{final}')
    except ValueError:
        pass


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="1 1 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

first = StringVar()
first_entry = ttk.Entry(mainframe, width=10, textvariable=first)
first_entry.grid(column=2, row=1, sticky=(W, E))
final = StringVar()
ttk.Label(mainframe, textvariable=final).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text='Считать', command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text='Введите число').grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text='').grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text='Результат').grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

first_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()
