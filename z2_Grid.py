from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign Up Page")
root.geometry("250x150")


name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1)

root.mainloop()