from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

entry_box = ttk.Entry(root, width=50, state='disabled')
entry_box.pack(padx=10, pady=10)

button_frame1 = Frame(root)
button_frame1.pack()

button_frame2 = Frame(root)
button_frame2.pack()

button_frame3 = Frame(root)
button_frame3.pack()

button_frame4 = Frame(root)
button_frame4.pack()


root.mainloop()