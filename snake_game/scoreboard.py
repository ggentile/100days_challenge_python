from turtle import Turtle


class Scoreboard(Turtle):

    with open("data.txt", mode="r") as file:
        previous_result = file.read()

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(Scoreboard.previous_result)
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score} High Score: {self.high_score}', align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as record:
                record.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
