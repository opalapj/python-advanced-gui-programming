import tkinter as tk
from tkinter import messagebox


def on_off_c():
    global switch_c
    if switch_c:
        button.config(command=lambda: None)
        button.config(text="Disable :(")
    else:
        button.config(command=click)
        button.config(text="Enable :)")
    switch_c = not switch_c


def on_off_nc():
    global switch_nc
    if switch_nc:
        label.unbind("<Button-1>")
        label.config(text="Disable :(")
    else:
        label.bind("<Button-1>", click)
        label.config(text="Enable :)")
    switch_nc = not switch_nc


def click(event=None):
    messagebox.showinfo("", "Confirmation!")


switch_c = True
switch_nc = True
window = tk.Tk()
button_c = tk.Button(window, text="Switch for clickable widget", command=on_off_c)
button_c.pack()
button = tk.Button(window, text="Enable :)", command=click)
button.pack()
button_nc = tk.Button(window, text="Switch for non-clickable widget", command=on_off_nc)
button_nc.pack()
label = tk.Label(window, text="Enable :)")
label.bind("<Button-1>", click)
label.pack()
window.mainloop()
