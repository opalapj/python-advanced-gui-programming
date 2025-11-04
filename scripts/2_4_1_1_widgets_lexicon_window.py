import tkinter as tk
from tkinter import messagebox


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 300:
            grows = True
    window.geometry("{0}x{0}".format(size))


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()

# Adding window title.
window.title("Orlen App")

# Adding window icon., 2 ways.
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))  # Ptyhon Institute proposal.
window.iconphoto(False, tk.PhotoImage(file="logo.png"))  # Simple package solution.

# Managing window size + extra callback.
# size = 300
# grows = True
# window.minsize(250, 250)
# window.maxsize(1000, 1000)
# window.geometry('{0}x{0}'.format(size))
# window.bind("<Button-1>", click)

# Using lambda as a callback.
# window.bind("<Button-1>", lambda e: window.destroy())

# Making window dimension resizable or not.
window.resizable(width=False, height=False)
# window.resizable(width=True, height=False)
window.geometry("400x200")

# Binding callback to the main window’s close operation.
window.protocol("WM_DELETE_WINDOW", really)

window.mainloop()
