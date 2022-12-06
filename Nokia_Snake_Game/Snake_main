from turtle import Screen
import snake
import food
import time
import scoreboard

# Set up screen and size
screen = Screen()
screen.setup(width=600, height=600)
# background color
screen.bgcolor("black")
# Title
screen.title("My Snake Game")

# Turn off the tracer
screen.tracer(0)

# create snake
snake = snake.Snake()

# Create food
food = food.Food()

# Create scoreboard
scoreboard = scoreboard.Scoreboard()

# keyboard control
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    # update every 0.1s
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score_up()
        # Food go to new random location
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # If head collides with any segment in the tail.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
