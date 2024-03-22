from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Login Page")
root.geometry("375x300")

username_label = ttk.Label(root, text="Username:")
username_label.place(x=50, y=50)
username_entry = ttk.Entry(root)
username_entry.place(x=150, y=50)

password_label = ttk.Label(root, text="Password:")
password_label.place(x=50, y=80)
password_entry = ttk.Entry(root)
password_entry.place(x=150, y=80)

root.mainloop()