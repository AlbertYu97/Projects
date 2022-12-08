import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []

    def add_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_color = random.choice(COLORS)
            new_car.color(random_color)
            new_car.setheading(180)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.car_list.append(new_car)

    def move_car(self, level):
        for index in range(len(self.car_list)):
            distance = STARTING_MOVE_DISTANCE + (level-1) * MOVE_INCREMENT
            new_x = self.car_list[index].xcor() - distance
            self.car_list[index].goto(new_x, self.car_list[index].ycor())








