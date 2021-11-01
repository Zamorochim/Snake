from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.new_food()

    def new_food(self):
        self.shape('turtle')
        self.penup()
        self.color('dark green')
        self.refresh()

    def refresh(self):
        new_x = random.randint(-370, 370)
        new_y = random.randint(-370, 370)
        self.goto(new_x, new_y)
