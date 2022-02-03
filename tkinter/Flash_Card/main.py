# -------------------------- imports --------------------------#
from tkinter import *
import pandas
import random

# -------------------------- global variables --------------------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_row = {}

# -------------------------- pandas read --------------------------#
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    data_row = original_data.to_dict(orient="records")
else:
    data_row = data.to_dict(orient="records")


# -------------------------- functions --------------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_row)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(changing_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image_front)
    flip_timer = window.after(3000, next_card_en)


def next_card_en():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(title, text="English", fill="white")
    english_word = current_card["English"]
    canvas.itemconfig(changing_text, text=english_word, fill="white")


def is_known():
    data_row.remove(current_card)
    words_to_know = pandas.DataFrame(data_row)
    words_to_know.to_csv("words_to_learn.csv", index=False)
    next_card()


# -------------------------- window config --------------------------#
window = Tk()

window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
window.title("Flash Card")

flip_timer = window.after(3000, next_card_en)

# -------------------------- images --------------------------#
image_front = PhotoImage(file="card_front.png")
image_back = PhotoImage(file="card_back.png")
image_correct = PhotoImage(file="right.png")
image_wrong = PhotoImage(file="wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 24, "italic"))
changing_text = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# -------------------------- Labels, Buttons --------------------------#
button_right = Button(image=image_correct, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

# -------------------------- code logic --------------------------#
next_card()

window.mainloop()
