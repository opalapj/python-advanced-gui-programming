import tkinter
from tkinter import messagebox


def click():
    messagebox.showinfo("info", "some\ninfo")


window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=click)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()
