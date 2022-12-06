import time
import turtle
import paddle
import ball
import time
import scoreboard

# create screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# Title name
screen.title("Pong")
# Turn off animation
screen.tracer(0)

# Create two paddles
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))

# Create a ball
ball = ball.Ball()

# Create scoreboard
scoreboard = scoreboard.Scoreboard()

# up and down
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_is_on = True
while game_is_on:
    # sleep 0.1s between each update
    time.sleep(ball.move_speed)
    # Animation is turn off, paddle is created and paddle is shown here
    screen.update()
    ball.move()
    # Detect collision with wall
    # when the ball hits the top/bottom edge, change the direction on the y-axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_edge()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.r_point()
        sleep_time = 0.1

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.l_point()

# click on exit
screen.exitonclick()
