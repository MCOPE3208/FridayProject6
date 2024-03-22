from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

entry_box = ttk.Entry(root, width=50, state='disabled')
entry_box.pack(padx=10, pady=10)


root.mainloop()