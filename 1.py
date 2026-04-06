import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="Welcome to your first GUI!")
label.pack()

button = tk.Button(root, text="Click Me",command=lambda: print("Oh you clicked me!"))
button.pack()

root.mainloop()