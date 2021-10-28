from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout")
screen.tracer(0)

brick_colors = ["yellow", "green", "cyan", "blue", "red"]

paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)
bricks = []


def new_stage():
    global bricks
    for y in range(0, 5):
        for x in range(-5, 5):
            bricks.append(Brick(brick_colors[y], (60 * x + 25, 30 * y), 10 * y + 10))


screen.listen()
screen.getcanvas().bind('<Motion>', paddle.go_position)

new_stage()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with bricks
    for brick in bricks:
        if brick.is_collided_with(ball):
            scoreboard.score += brick.point
            scoreboard.update_scoreboard()
            bricks.remove(brick)
            brick.reset()
            ball.move_speed *= 1.01
            ball.bounce_y()

    # Detect collision with left and right wall
    if ball.xcor() + 10 > SCREEN_WIDTH/2 or ball.xcor() - 10 < -SCREEN_WIDTH/2:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() + 10 > SCREEN_HEIGHT/2:
        ball.bounce_y()

    # Detect collision with paddle
    if paddle.is_collided_with(ball):
        ball.bounce_y()
        # Stage Cleared
        if not bricks:
            scoreboard.level += 1
            scoreboard.update_scoreboard()
            new_stage()

    # Detect paddle misses
    if ball.ycor() < -SCREEN_HEIGHT/2:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
