import random
import tkinter as tk


class Clicker:
    def __init__(self, size):
        size = size
        self.numbers = random.sample(range(1, 1000), size**2)
        root = tk.Tk()
        root.title("Clicker")
        for i in range(size**2):
            button = tk.Button(root, text=self.numbers[i], width=10)
            button.grid(row=i // size, column=i % size)
            button.bind("<Button-1>", self.click)
        self.numbers.sort()
        self.time = tk.IntVar()
        self.label = tk.Label(root, textvariable=self.time)
        self.label.grid(row=size + 1, columnspan=size)
        self.clock_started = False
        root.mainloop()

    def clock(self):
        if self.numbers:
            self.time.set(self.time.get() + 1)
            self.label.after(1000, self.clock)

    def click(self, event):
        if not self.clock_started:
            self.clock_started = True
            self.label.after(1000, self.clock)
        button_ = event.widget
        if button_.cget("text") == self.numbers[0]:
            button_.config(state=tk.DISABLED)
            self.numbers.pop(0)


app = Clicker(size=10)
