import random
import tkinter as tk


def clock():
    if numbers:
        time.set(time.get() + 1)
        label.after(1000, clock)


def click(event):
    global clock_started
    if not clock_started:
        clock_started = True
        label.after(1000, clock)
    button_ = event.widget
    if button_.cget("text") == numbers[0]:
        button_.config(state=tk.DISABLED)
        numbers.pop(0)


size = 2
numbers = random.sample(range(1, 1000), size**2)
root = tk.Tk()
root.title("Clicker")
for i in range(size**2):
    button = tk.Button(root, text=numbers[i], width=10)
    button.grid(row=i // size, column=i % size)
    button.bind("<Button-1>", click)
numbers.sort()
time = tk.IntVar()
label = tk.Label(root, textvariable=time)
label.grid(row=size + 1, columnspan=size)
clock_started = False
root.mainloop()
