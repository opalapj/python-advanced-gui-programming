import tkinter as tk
from tkinter import messagebox as msg


def evaluate():
    values = []
    for entry in filter(lambda x: isinstance(x, tk.Entry), root.children.values()):
        try:
            values.append(float(entry.get()))
        except ValueError:
            msg.showerror(title="Evaluation's error", message="Invalid data!")
            entry.focus_set()
            return
    if radio_var.get() == 0:
        result = values[0] + values[1]
    elif radio_var.get() == 1:
        result = values[0] - values[1]
    elif radio_var.get() == 2:
        result = values[0] * values[1]
    else:
        try:
            result = values[0] / values[1]
        except ZeroDivisionError:
            msg.showerror(title="Evaluation's error", message="Division by zero!")
            return
    msg.showinfo(title="Evaluation's error", message=str(result))


root = tk.Tk()
root.title("Calculator")
root.iconphoto(False, tk.PhotoImage(file="logo.png"))
entry_left = tk.Entry(root)
entry_right = tk.Entry(root)
radio_var = tk.IntVar()
radio_addition = tk.Radiobutton(root, text="+", variable=radio_var, value=0)
radio_subtraction = tk.Radiobutton(root, text="-", variable=radio_var, value=1)
radio_multiplication = tk.Radiobutton(root, text="*", variable=radio_var, value=2)
radio_division = tk.Radiobutton(root, text="/", variable=radio_var, value=3)
button = tk.Button(root, text="Evaluate", command=evaluate)
entry_left.grid(row=1, column=0, rowspan=2)
entry_right.grid(row=1, column=2, rowspan=2)
radio_addition.grid(row=0, column=1)
radio_subtraction.grid(row=1, column=1)
radio_multiplication.grid(row=2, column=1)
radio_division.grid(row=3, column=1)
button.grid(row=4, column=1)
entry_left.focus_set()
root.mainloop()
