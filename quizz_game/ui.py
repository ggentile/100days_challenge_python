from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        image_correct = PhotoImage(file="right.png")
        image_wrong = PhotoImage(file="wrong.png")
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="",
                                            font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="white",
                           font=("Ariel", 14, "bold"))
        self.score.grid(row=0, column=1)

        self.button_right = Button(image=image_correct, highlightthickness=0, command=self.true_pressed)
        self.button_right.grid(row=2, column=0)
        self.button_wrong = Button(image=image_wrong, highlightthickness=0, command=self.false_pressed)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end"
                                                   "of the quizz!")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(self.canvas, bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")
        self.window.after(1000, self.get_next_question)
