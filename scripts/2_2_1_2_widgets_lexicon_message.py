import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
text.set("You did it again... ")
message = tk.Message(window, textvariable=text, width=200)
message.pack()
# I do not see any differences between message and label.
# label = tk.Message(window, textvariable=text, width=200)
# label.pack()
window.mainloop()
