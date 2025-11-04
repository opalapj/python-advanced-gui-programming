import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


def u_observer(*args):
    print("Unsetting")


dummy = tk.Tk()  # We need this, although we won't display any windows.
str_var = tk.StringVar()
str_var.set("abc")
# Observer is a function (a kind of callback) which will be invoked
# automatically each time a specified event occurs in the variable’s life
r_obs_id = str_var.trace_add(
    "read", r_observer
)  # Adding observer for reading str_var control variable.
w_obs_id = str_var.trace_add(
    "write", w_observer
)  # Adding observer for writing str_var control variable.
u_obs_id = str_var.trace_add(
    "unset", u_observer
)  # Adding observer for unsetting str_var control variable.
str_var.set(str_var.get() + "d")  # Read nested in write.
str_var.trace_remove(
    "read", r_obs_id
)  # Deleting observer for reading str_var control variable.
str_var.set(str_var.get() + "e")  # Read nested in write.
str_var.trace_remove(
    "write", w_obs_id
)  # Deleting observer for writing str_var control variable.
str_var.set(str_var.get() + "f")  # Read nested in write.
print(str_var.get())
del str_var
try:
    print(str_var.get())
except NameError as e:
    print(e)
    print("Printing failed.")
finally:
    print("It wasn't for lack of trying.")
