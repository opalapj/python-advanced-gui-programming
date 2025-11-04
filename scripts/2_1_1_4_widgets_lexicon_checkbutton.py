import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo(
        title="Summary",
        message="Counter: " + str(counter) + "\nState: " + str(switch.get()),
        icon=messagebox.ERROR,
        # icon='error'
    )


window = tk.Tk()
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.after(1000, checkbutton.invoke)  # Mark tick after 1000 ms.
checkbutton.pack()
window.mainloop()
