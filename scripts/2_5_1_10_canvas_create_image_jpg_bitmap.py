import tkinter as tk

from PIL import Image
from PIL import ImageTk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="red")
jpg = Image.open("data/logo.jpg")
image = ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
