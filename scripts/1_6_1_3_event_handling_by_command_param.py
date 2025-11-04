import tkinter as tk
from tkinter import messagebox


def click():
    messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)
# button.pack()

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack()

window.mainloop()
