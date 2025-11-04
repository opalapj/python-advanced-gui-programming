import tkinter as tk


class Calculator:
    def __init__(self):
        self.operation_ = ""
        self.memory = 0
        self.ERROR = "Error"
        root = tk.Tk()
        self.display = tk.StringVar(value="0")
        entry = tk.Entry(
            root,
            font=("Consolas", "15", "bold"),  # Monospace typeface.
            width=10,
            textvariable=self.display,
            justify=tk.RIGHT,
            state="readonly",  # Prevent keyboard input.
            readonlybackground="white",
        )
        entry.grid(row=0, columnspan=5)
        btn_0 = tk.Button(root, text=0, width=3)
        btn_0.bind("<Button-1>", self.digit)
        btn_0.grid(row=4, column=0)
        btn_1 = tk.Button(root, text=1, width=3)
        btn_1.bind("<Button-1>", self.digit)
        btn_1.grid(row=3, column=0)
        btn_2 = tk.Button(root, text=2, width=3)
        btn_2.bind("<Button-1>", self.digit)
        btn_2.grid(row=3, column=1)
        btn_3 = tk.Button(root, text=3, width=3)
        btn_3.bind("<Button-1>", self.digit)
        btn_3.grid(row=3, column=2)
        btn_4 = tk.Button(root, text=4, width=3)
        btn_4.bind("<Button-1>", self.digit)
        btn_4.grid(row=2, column=0)
        btn_5 = tk.Button(root, text=5, width=3)
        btn_5.bind("<Button-1>", self.digit)
        btn_5.grid(row=2, column=1)
        btn_6 = tk.Button(root, text=6, width=3)
        btn_6.bind("<Button-1>", self.digit)
        btn_6.grid(row=2, column=2)
        btn_7 = tk.Button(root, text=7, width=3)
        btn_7.bind("<Button-1>", self.digit)
        btn_7.grid(row=1, column=0)
        btn_8 = tk.Button(root, text=8, width=3)
        btn_8.bind("<Button-1>", self.digit)
        btn_8.grid(row=1, column=1)
        btn_9 = tk.Button(root, text=9, width=3)
        btn_9.bind("<Button-1>", self.digit)
        btn_9.grid(row=1, column=2)
        btn_clear = tk.Button(root, text="C", width=3, command=self.clear)
        btn_clear.grid(row=4, column=1)
        btn_dec_point = tk.Button(root, text=".", width=3)
        btn_dec_point.bind("<Button-1>", self.dec_point)
        btn_dec_point.grid(row=4, column=2)
        btn_result = tk.Button(root, text="=", width=3, command=self.result)
        btn_result.grid(row=3, column=3)
        btn_sign = tk.Button(root, text="+/-", width=3, command=self.sign)
        btn_sign.grid(row=4, column=3)
        btn_add = tk.Button(root, text="+", width=3)
        btn_add.bind("<Button-1>", self.operation)
        btn_add.grid(row=1, column=4)
        btn_sub = tk.Button(root, text="-", width=3)
        btn_sub.bind("<Button-1>", self.operation)
        btn_sub.grid(row=2, column=4)
        btn_mul = tk.Button(root, text="*", width=3)
        btn_mul.bind("<Button-1>", self.operation)
        btn_mul.grid(row=3, column=4)
        btn_div = tk.Button(root, text="/", width=3)
        btn_div.bind("<Button-1>", self.operation)
        btn_div.grid(row=4, column=4)
        root.mainloop()

    def clear(self):
        self.display.set("0")
        self.operation_ = ""
        self.memory = 0

    def clear_error(self):
        self.clear() if self.display.get() == self.ERROR else None

    def display_length_cond(self):
        return True if len(self.display.get()) < 10 else False

    def beauty(self, number):
        number = str(number)
        if "e" not in number and number.find(".") <= 10:
            number = number[:10]
            if "." in number:
                number = number.rstrip("0")
                if number[-1] == ".":
                    return number[:-1]
                else:
                    return number
            else:
                return number
        else:
            return self.ERROR

    def result(self):
        if self.operation_ != "":
            value = float(self.display.get())
            if self.operation_ == "+":
                self.memory += value
            elif self.operation_ == "-":
                self.memory -= value
            elif self.operation_ == "*":
                self.memory *= value
            else:
                try:
                    self.memory /= value
                except ZeroDivisionError:
                    self.display.set(self.ERROR)
                    return
        self.display.set(self.beauty(self.memory))

    def operation(self, event):
        self.clear_error()
        self.operation_ = event.widget.cget("text")
        self.memory = float(self.display.get())
        self.display.set("0")

    def digit(self, event):
        self.clear_error()
        if self.display_length_cond():
            digit_ = str(event.widget.cget("text"))
            if self.display.get() == "0":
                self.display.set(digit_)
            else:
                self.display.set(self.display.get() + digit_)

    def dec_point(self, event):
        self.clear_error()
        dec_point_ = event.widget.cget("text")
        if dec_point_ not in self.display.get() and self.display_length_cond():
            self.display.set(self.display.get() + dec_point_)

    def sign(self):
        self.clear_error()
        if self.display.get()[0] == "-":
            self.display.set(self.display.get()[1:])
        elif self.display.get() != "0" and self.display_length_cond():
            self.display.set("-" + self.display.get())


app = Calculator()
