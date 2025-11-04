import tkinter as tk
from tkinter import font


window = tk.Tk()

# Declared as a tuple.
label_0 = tk.Label(
    window, text="24-point Times bold italic", font=("Times", 24, "bold")
)
label_0.grid(column=0, row=0)

label_1 = tk.Label(window, text="16-point Arial regular", font=("Arial", "16"))
label_1.grid(column=0, row=1)

# Created by user.
my_font = font.Font(
    family="Arial",
    size=36,
    weight="bold",
    slant="italic",
    underline=True,
    overstrike=True,
)
# label_2 = tk.Label(window, text="36-point underline overstrike Arial bold italic", font=my_font)  # Instead of:
label_2 = tk.Label(
    window,
    text="36-point underline overstrike Arial bold italic",
    font=("Arial", 36, "bold italic underline overstrike"),
)
label_2.grid(column=0, row=2)

# Standard Font.
label_3 = tk.Label(window, text="TkTextFont", font="TkFixedFont")
label_3.grid(column=0, row=3)

label_4 = tk.Label(window, text="Default for label widget")
label_4.grid(column=0, row=4)

# Platfrom-specific Font.
label_5 = tk.Label(window, text="systemfixed", font="systemfixed")
label_5.grid(column=0, row=5)

font_list = sorted(list(font.names()))
for f in font_list:
    print(f"{f:20} -> {font.nametofont(f).actual()}")

for f in font.families():
    print(f)

window.mainloop()
