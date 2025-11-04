import tkinter as tk
from tkinter import messagebox


def click(event=None):
    # Parameter 'event' seems tu be useful, but when function
    # the parameter is located in is invoked by event created with bind method,
    # then it brings some information.
    if event is None:
        messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = (
            "x="
            + str(event.x)
            + "\ny="
            + str(event.y)
            + "\nnum="
            + str(event.num)
            + "\ntype="
            + event.type
        )
        messagebox.showinfo("Click!", string)


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)  # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)  # Line II
frame.pack()

window.mainloop()
