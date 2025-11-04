import tkinter as tk


l_colors = ["#FF0000", "#FFFF00", "#008000"]
l_phases = (
    (True, False, False),
    (True, True, False),
    (False, False, True),
    (False, True, False),
)
l_border = 3
l_space = 10
l_diameter = 150


def switch():
    global phase
    phase = phase % len(l_phases)
    for oval_id, oval in enumerate(canvas.find_all()):
        canvas.itemconfigure(
            oval, state=tk.NORMAL if l_phases[phase][oval_id] else tk.DISABLED
        )
    phase += 1


root = tk.Tk()
canvas = tk.Canvas(
    root,
    width=l_diameter + 2 * l_space,
    height=len(l_colors) * (l_diameter + l_space) + l_space,
    bg="#555555",
)
for i in range(len(l_colors)):
    canvas.create_oval(
        l_space + l_border,
        (l_space + l_border) + i * (l_space + l_diameter),
        l_space + l_diameter,
        (i + 1) * (l_space + l_diameter),
        width=l_border,
        fill=l_colors[i],
        disabledfill="#808080",
        state=tk.DISABLED,
    )
canvas.grid(row=0)
button_next = tk.Button(root, text="Next", command=switch)
button_next.grid(row=1)
button_quit = tk.Button(root, text="Quit", command=root.destroy)
button_quit.grid(row=2)
phase = 0
switch()
root.mainloop()
