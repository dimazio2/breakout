from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, position, point):
        super().__init__()
        self.point = point;
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(position)

    def is_collided_with(self, ball):
        if (ball.xcor() > self.xcor() - 25) and (ball.xcor() < self.xcor() + 25) and \
           (ball.ycor() + 10 > self.ycor() - 10) and (ball.ycor() - 10 < self.ycor() + 10):
            return True
        return False

