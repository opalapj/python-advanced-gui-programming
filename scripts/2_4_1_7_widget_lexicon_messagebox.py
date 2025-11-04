from tkinter import messagebox as msg


msg.askyesno()
answer = msg.askyesno(
    title="Custom title",
    message='Custom message, "No" button as a default choice, warning as a icon and writing answer as variable.',
    default=msg.NO,
    icon=msg.WARNING,
)
print(answer)

answer = msg.askquestion(
    title="Custom title",
    message='Custom message, "No" button as a default choice, warning as a icon and writing answer as variable.',
    default=msg.NO,
    icon=msg.WARNING,
)
print(answer)

answer = msg.askretrycancel(
    title="Custom title",
    message='Custom message, "No" button as a default choice, warning as a icon and writing answer as variable.',
    icon=msg.WARNING,
)
print(answer)
