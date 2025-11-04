import tkinter as tk


def clock():
    global extent
    extent -= 20
    canvas.itemconfigure(1, extent=extent)
    window.after(1000, clock)


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
extent = 0
arc = canvas.create_arc(
    10, 100, 380, 300, outline="red", width=5, start=90, extent=extent
)
canvas.create_arc(
    10, 100, 380, 300, outline="blue", width=5, style=tk.CHORD, start=90, fill="white"
)
canvas.create_arc(
    10, 100, 380, 300, outline="green", width=5, style=tk.ARC, start=180, extent=180
)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.after(1000, clock)
window.mainloop()
