import tkinter as tk


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))  # Ad 1st method.
    label_1["text"] = to_string(counter)  # Ad 2nd method.


counter = 0
window = tk.Tk()
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
# 1st method to make dynamic changed label text, via control variable and textvariable parameter.
text = tk.StringVar()
label_0 = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label_0.pack()
# 2nd method to make dynamic changed label text, via text parameter.
label_1 = tk.Label(window, text=to_string(counter), height=4)
label_1.pack()
window.mainloop()
