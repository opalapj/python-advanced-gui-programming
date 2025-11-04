import random
import tkinter as tk


class Game:
    def __init__(self, window_width, window_height, pad_x=10, pad_y=10):
        self.root_width = window_width
        self.root_height = window_height
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.x, self.y = self.pad_x, self.pad_y
        root = tk.Tk()
        root.geometry("{}x{}".format(self.root_width, self.root_height))
        root.title("Catch me!")
        self.button = tk.Button(root, text="Catch me!")
        self.button.bind("<Enter>", self.move)
        self.button.place(x=self.x, y=self.y)
        root.mainloop()

    def move(self, event):
        x_new = random.randint(
            self.pad_x, self.root_width - self.pad_x - self.button.winfo_width()
        )
        y_new = random.randint(
            self.pad_y, self.root_height - self.pad_y - self.button.winfo_height()
        )
        while (
            abs(x_new - self.x) < self.button.winfo_width()
            and abs(y_new - self.y) < self.button.winfo_height()
        ):
            x_new = random.randint(
                self.pad_x, self.root_width - self.pad_x - self.button.winfo_width()
            )
            y_new = random.randint(
                self.pad_y, self.root_height - self.pad_y - self.button.winfo_height()
            )
        self.x = x_new
        self.y = y_new
        self.button.place(x=self.x, y=self.y)


app = Game(window_width=150, window_height=72)
