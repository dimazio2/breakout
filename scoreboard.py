from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.level = 1
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-120, screen_height/2 - 40)
        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level} Score:{self.score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
