import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.create_polygon(
    10, 380, 200, 10, 380, 380, fill="red", smooth=True, width=3, activedash=(10, 1)
)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
