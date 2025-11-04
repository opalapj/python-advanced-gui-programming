import tkinter as tk


window = tk.Tk()

button_1 = tk.Button(window, text="Ordinary button")
button_1.pack()

button_2 = tk.Button(window, text="Exceptional button", command=lambda: None)
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 5
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
# button_2['state'] = tk.DISABLED

button_3 = tk.Button(window, text="Colorful button")
button_3.pack()
button_3.config(bg="#000000")
button_3.config(fg="yellow")
button_3.config(activeforeground="#FF0000")
button_3.config(activebackground="green")

button_4 = tk.Button(window, text="Regular button")
button_4["anchor"] = "e"
button_4["width"] = 20
button_4["height"] = 5
button_4.pack()

button_5 = tk.Button(window, text="Another button")
button_5["anchor"] = "sw"
button_5["width"] = 20
button_5["height"] = 3
button_5.pack()

window.mainloop()
