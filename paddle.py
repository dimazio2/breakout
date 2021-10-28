from turtle import Turtle

STARTING_POSITION = (320, 240)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Paddle(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -screen_height/2 + 30)

    def go_position(self, event):
        self.goto(event.x - self.screen_width/2, self.ycor())

    def is_collided_with(self, ball):
        if (ball.xcor() > self.xcor() - 50) and (ball.xcor() < self.xcor() + 50) and \
           (ball.ycor() + 10 > self.ycor() - 10) and (ball.ycor() - 10 < self.ycor() + 10):
            return True
        return False
