import tkinter as tk


def on_off():
    state = button["text"]  # 1st way to read widget property.
    # state = button.cget("text")  # 2nd way to read widget property.
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state  # 1st way to write property.
    # button.config(text=state)  # 2nd way to write property.


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()
