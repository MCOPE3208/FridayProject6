from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Sign Up Page")
root.geometry("250x150")

name_label = ttk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1)

email_label = ttk.Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry = ttk.Entry(root)
email_entry.grid(row=1, column=1)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=2, column=0)
password_entry = ttk.Entry(root)
password_entry.grid(row=2, column=1)

root.mainloop()