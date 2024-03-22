from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

entry_box = Entry(root, width=50, state='disabled')
entry_box.pack(padx=10, pady=10)
entry_box.config(relief="solid")

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

btn4 = ttk.Button(button_frame2, text = 4)
btn4.pack(side = "left")

btn5 = ttk.Button(button_frame2, text = 5)
btn5.pack(side = "left")

btn6 = ttk.Button(button_frame2, text = 6)
btn6.pack(side = "left")

btnmultiply = ttk.Button(button_frame2, text = "x")
btnmultiply.pack(side = "left")

btn1 = ttk.Button(button_frame3, text = 1)
btn1.pack(side = "left")

btn2 = ttk.Button(button_frame3, text = 2)
btn2.pack(side = "left")

btn3 = ttk.Button(button_frame3, text = 3)
btn3.pack(side = "left")

btnsubtract = ttk.Button(button_frame3, text = "-")
btnsubtract.pack(side = "left")

btn0 = ttk.Button(button_frame4, text = 0)
btn0.pack(side = "left")

btndecimal = ttk.Button(button_frame4, text = ".")
btndecimal.pack(side = "left")

btnclear = ttk.Button(button_frame4, text = "C")
btnclear.pack(side = "left")

btnadd = ttk.Button(button_frame4, text = "+")
btnadd.pack(side = "left")

root.mainloop()