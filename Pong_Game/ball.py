from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + 10 * self.x_direction
        new_y = self.ycor() + 10 * self.y_direction
        self.goto(new_x, new_y)

    def bounce_edge(self):
        # Need to bounce
        self.y_direction *= -1
        self.move()

    def bounce_paddle(self):
        self.x_direction *= -1
        self.move_speed *= 0.9
        self.move()

    def reset_ball(self):
        self.goto(0, 0)
        self.x_direction *= -1
        self.move_speed = 0.1


