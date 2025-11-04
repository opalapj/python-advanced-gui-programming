import tkinter as tk


def switch():
    if button_1.cget("state") == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)


def mouseover(event):
    button_1["bg"] = "green"
    label["text"] = button_1["state"]


def mouseout(event):
    button_1["bg"] = "red"
    label["text"] = button_1["state"]


window = tk.Tk()
button_1 = tk.Button(window, text="Enabled", bg="red", activebackground="yellow")
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()
label = tk.Label(window, text=button_1["state"])
label.pack()
window.mainloop()
