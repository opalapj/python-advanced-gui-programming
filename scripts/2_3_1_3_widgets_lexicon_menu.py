import tkinter as tk
from tkinter import messagebox


def command_open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


def command_quit(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        root.destroy()


def command_about():
    messagebox.showinfo("App", "The application\nthat does nothing")


# 0. Root window creation.
root = tk.Tk()
# 0.0. Menu creation.
menu = tk.Menu(root)
root.config(  # Root (Toplevel widget) as a widget can be configure by .config() method.
    height=200, width=300, menu=menu
)
root.title("Orlen NERapp")
root.minsize(250, 150)
root.maxsize(350, 250)
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='logo.png'))  # Ptyhon Institute proposal.
root.iconphoto(False, tk.PhotoImage(file="logo.png"))  # Simple package solution.
# 0.0.0. 1st menu item/choice.
cascade_file = tk.Menu(menu, tearoff=0)
menu.add("cascade", label="File", underline=0, menu=cascade_file)
# 0.0.0.0. Add the Open action to the cascade_file submenu.
cascade_file.add("command", label="Open...", underline=0, command=command_open_file)
# 0.0.0.1. Add the OpenRecentFile action to the cascade_file submenu.
cascade_recent = tk.Menu(cascade_file, tearoff=0)
cascade_file.add(
    "cascade", label="Open recent file...", underline=1, menu=cascade_recent
)
# 0.0.0.1.0. - 0.0.0.1.4. Add 5 recent files.
for file in range(5):
    cascade_recent.add("command", label="{}. file.txt".format(file + 1), underline=0)
# 0.0.0.2. Add the separator to the cascade_file submenu.
cascade_file.add("separator")
# 0.0.0.3. Add the Quit action to the cascade_file submenu.
cascade_file.add(
    "command",
    label="Quit",
    underline=0,
    command=command_quit,
    accelerator="Ctrl+Q",  # It is only text. Event and callback need to be implemented separately.
)
cascade_file.entryconfig(
    3, background="red"
)  # Quit (command item) as a item can not be configure by .config() method. It has to be .entryconfig().
# 0.0.1. 2nd menu item.
menu.add("command", label="About...", command=command_about, underline=1)
root.bind_all(
    "<Control-KeyPress-q>", command_quit
)  # Implemented event for Ctrl+Q hot key.
root.mainloop()
