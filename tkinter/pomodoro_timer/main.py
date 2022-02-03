from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
    checkbox.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        start_clock(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        start_clock(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK)
    else:
        start_clock(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_clock(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, start_clock, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✅"
        checkbox.config(text="✅")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, fg=GREEN, highlightthickness=0,
                      font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=YELLOW, fg=GREEN, highlightthickness=0,
                      font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

checkbox = Label(bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 12, "bold"))
checkbox.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 114, image=tomato_img)
canvas.grid(column=1, row=2)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


window.mainloop()
