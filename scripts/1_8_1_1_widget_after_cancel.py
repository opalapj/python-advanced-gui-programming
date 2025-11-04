import tkinter as tk
from tkinter import messagebox


def blink():
    global is_white
    global counter
    if is_white:
        color = "black"
    else:
        color = "white"
    is_white = not is_white
    frame.config(bg=color)
    msg = str(counter) + " change complete, click OK to next iteration."
    messagebox.showinfo(message=msg)
    f = frame.after(1000, blink)
    counter += 1
    if counter > 3:
        frame.after_cancel(f)
        msg = str(counter) + ". iteration canceled."
        messagebox.showinfo(message=msg)


is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg="white")
frame.after(1000, blink)
counter = 1
frame.pack()
window.mainloop()
