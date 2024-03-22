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

btn7 = ttk.Button(button_frame1, text = 7)
btn7.pack(side = "left")

btn8 = ttk.Button(button_frame1, text = 8)
btn8.pack(side = "left")

btn9 = ttk.Button(button_frame1, text = 9)
btn9.pack(side = "left")

btndivide = ttk.Button(button_frame1, text = "/")
btndivide.pack(side = "left")

root.mainloop()