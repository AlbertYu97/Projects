from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.level = 1
        self.goto(STARTING_POSITION)

    # Define go_up function
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Define reset position function
    def reset_position(self):
        self.level += 1
        self.goto(STARTING_POSITION)
