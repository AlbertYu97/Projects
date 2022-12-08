import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create classes
player = Player()
car = CarManager()
scoreboard = Scoreboard()

# Allow the player to move
screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    # Update the screen once every 0.1s
    time.sleep(0.1)
    screen.update()

    # Update scoreboard
    scoreboard.update_scoreboard(player.level)
    # Add new car and let the cars move together
    car.add_car()
    car.move_car(player.level)

    # Detect collision
    for element in car.car_list:
        if player.distance(element.position()) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Player reaches top and move to next level
    if player.ycor() > 280:
        player.reset_position()

screen.exitonclick()


