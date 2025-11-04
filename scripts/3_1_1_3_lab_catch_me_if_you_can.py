import random
import tkinter as tk


def move(event):
    global x, y
    x_new = random.randint(pad_x, root_width - pad_x - button.winfo_width())
    while abs(x_new - x) < button.winfo_width():
        x_new = random.randint(pad_x, root_width - pad_x - button.winfo_width())
    x = x_new
    y_new = random.randint(pad_y, root_height - pad_y - button.winfo_height())
    while abs(y_new - y) < button.winfo_height():
        y_new = random.randint(pad_y, root_height - pad_y - button.winfo_height())
    y = y_new
    button.place(x=x, y=y)


root_width, root_height = 500, 500
pad_x, pad_y = 10, 10
x, y = pad_x, pad_y
root = tk.Tk()
root.geometry("{}x{}".format(root_width, root_height))
root.title("Catch me!")
button = tk.Button(root, text="Catch me!")
button.bind("<Enter>", move)
button.place(x=x, y=y)
root.mainloop()
