import tkinter as tk

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="🍌")
password_entry.pack()

def login():
    print("Username:", username_entry.get())
    print("Password:", password_entry.get())

def already():
    print(" Ano Baka ")
tk.Button(root, text="Login", command=login).pack()
tk.Button(root, text="already have a account", command=already).pack()

root.mainloop()