import tkinter as tk


def suicide(w):
    w.destroy()


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg="green")
button = tk.Button(frame, text="I'm a frame's child")
button.after(2000, suicide, button)
button.place(x=10, y=10)
frame.after(4000, suicide, frame)
frame.pack()
window.after(6000, suicide, window)
window.mainloop()
