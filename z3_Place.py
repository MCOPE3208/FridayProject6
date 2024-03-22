from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Login Page")
root.geometry("375x300")

username_label = ttk.Label(root, text="Username:")
username_label.place(x=50, y=50)
username_entry = ttk.Entry(root)
username_entry.place(x=150, y=50)

root.mainloop()