from tkinter import *


def make_calculus():
    miles = float(entry.get())
    result = miles * 1.609
    entry_converter.config(text=result)


window = Tk()

window.title("Miles converter")
window.minsize(width=400, height=50)

entry = Entry(width=5)
entry.grid(column=2, row=0)
label_first_line = Label(text="Miles")
label_first_line.grid(column=3, row=0)
label_second_line = Label(text="is equal to")
label_second_line.grid(column=1, row=1)
entry_converter = Label(width=5, text="0")
entry_converter.grid(column=2, row=1)
last_label = Label(text="Km")
last_label.grid(column=3, row=1)
button_calculate = Button(text="Calculate", command=make_calculus)
button_calculate.grid(column=2, row=2)


window.mainloop()
