import tkinter as tk
from tkinter import messagebox as msg


class Calculator:
    def __init__(self, name, logo):
        name = name
        logo = logo
        self.root = tk.Tk()
        self.root.title(name)
        self.root.iconphoto(False, tk.PhotoImage(file=logo))
        entry_left = tk.Entry(self.root)
        entry_right = tk.Entry(self.root)
        self.radio_var = tk.IntVar()
        radio_addition = tk.Radiobutton(
            self.root, text="+", variable=self.radio_var, value=0
        )
        radio_subtraction = tk.Radiobutton(
            self.root, text="-", variable=self.radio_var, value=1
        )
        radio_multiplication = tk.Radiobutton(
            self.root, text="*", variable=self.radio_var, value=2
        )
        radio_division = tk.Radiobutton(
            self.root, text="/", variable=self.radio_var, value=3
        )
        button = tk.Button(self.root, text="Evaluate", command=self.evaluate)
        entry_left.grid(row=1, column=0, rowspan=2)
        entry_right.grid(row=1, column=2, rowspan=2)
        radio_addition.grid(row=0, column=1)
        radio_subtraction.grid(row=1, column=1)
        radio_multiplication.grid(row=2, column=1)
        radio_division.grid(row=3, column=1)
        button.grid(row=4, column=1)
        entry_left.focus_set()
        self.root.mainloop()

    def evaluate(self):
        values = []
        for entry in filter(
            lambda x: isinstance(x, tk.Entry), self.root.children.values()
        ):
            try:
                values.append(float(entry.get()))
            except ValueError:
                msg.showerror(title="Evaluation's error", message="Invalid data!")
                entry.focus_set()
                return
        if self.radio_var.get() == 0:
            result = values[0] + values[1]
        elif self.radio_var.get() == 1:
            result = values[0] - values[1]
        elif self.radio_var.get() == 2:
            result = values[0] * values[1]
        else:
            try:
                result = values[0] / values[1]
            except ZeroDivisionError:
                msg.showerror(title="Evaluation's error", message="Division by zero!")
                return
        msg.showinfo(title="Evaluation's error", message=str(result))


app = Calculator(name="Orlen Calculator", logo="logo.png")
