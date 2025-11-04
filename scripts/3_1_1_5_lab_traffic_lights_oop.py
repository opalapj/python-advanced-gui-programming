import tkinter as tk


class Lights:
    def __init__(self, colors_, phases_, border=3, space=10, diameter=150):
        root = tk.Tk()
        self.phases = phases_
        self.canvas = tk.Canvas(
            root,
            width=diameter + 2 * space,
            height=len(colors_) * (diameter + space) + space,
            bg="#555555",
        )
        for i in range(len(colors_)):
            self.canvas.create_oval(
                space + border,
                (space + border) + i * (space + diameter),
                space + diameter,
                (i + 1) * (space + diameter),
                width=border,
                fill=colors_[i],
                disabledfill="#808080",
                state=tk.DISABLED,
            )
        self.canvas.grid(row=0)
        button_next = tk.Button(root, text="Next", command=self.switch)
        button_next.grid(row=1)
        button_quit = tk.Button(root, text="Quit", command=root.destroy)
        button_quit.grid(row=2)
        self.phase = 0
        self.switch()
        root.mainloop()

    def switch(self):
        phase = self.phase % len(self.phases)
        for oval_id, oval in enumerate(self.canvas.find_all()):
            self.canvas.itemconfigure(
                oval, state=tk.NORMAL if self.phases[phase][oval_id] else tk.DISABLED
            )
        self.phase += 1


colors = ["#FF0000", "#FFFF00", "#008000"]
phases = (
    (True, False, False),
    (True, True, False),
    (False, False, True),
    (False, True, False),
)
# colors = ['white', 'black']
# phases = ((True, False),
#           (True, True),
#           (False, True),
#           (True, True))
app = Lights(colors, phases)
