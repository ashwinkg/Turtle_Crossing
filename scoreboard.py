from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.current_level = 1
        self.print_score_card()

    def print_score_card(self):
        self.clear()
        self.write(arg=f"Level: {self.current_level}", move=False, align="left", font=FONT)

    def update_level(self):
        self.current_level += 1
        self.print_score_card()

    def print_game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT)
