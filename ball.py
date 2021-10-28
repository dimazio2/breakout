from turtle import Turtle


class Ball(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto((-screen_width/2 + 40, -40))
        self.x_move = 1.5
        self.y_move = -1.5
        self.move_speed = 1.4

    def move(self):
        new_x = self.xcor() + self.move_speed * self.x_move
        new_y = self.ycor() + self.move_speed * self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.goto((-self.screen_width/2 + 40, -40))
        self.x_move = 1.5
        self.y_move = -1.5
        self.move_speed = 0.1
