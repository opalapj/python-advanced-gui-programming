import tkinter as tk
from tkinter import messagebox as msg


def digits_only(*args):
    # msg.showinfo(message='in callback')
    global last_string
    string = text.get()
    # string = entry.get()  # String can be gotten also from entry widget.
    msg.showinfo(message=string)
    # Only digit with max 5 characters.
    if (string == "" or string.isdigit()) and len(
        string
    ) <= 5:  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)


last_string = ""
window = tk.Tk()
text = tk.StringVar(value=last_string)
entry = tk.Entry(window, textvariable=text)
text.trace("w", digits_only)
entry.pack()
entry.focus_set()  # Very helpful, direct input focus to this widget.
window.mainloop()
